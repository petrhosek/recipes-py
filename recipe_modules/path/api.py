# Copyright 2013 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import functools
import os
import sys
import tempfile

from recipe_engine import recipe_api
from recipe_engine import config_types


class Error(Exception):
  """Error specific to path recipe module."""


def PathToString(api, test):
  def PathToString_inner(path):
    assert isinstance(path, config_types.Path)
    base_path = path.base.resolve(test.enabled)
    suffix = path.platform_ext.get(api.m.platform.name, '')
    return api.join(base_path, *path.pieces) + suffix
  return PathToString_inner


def string_filter(func):
  @functools.wraps(func)
  def inner(*args, **kwargs):
    return func(*map(str, args), **kwargs)
  return inner


class path_set(object):
  """ implements a set which contains all the parents folders of added folders.
  """
  def __init__(self, path_mod, initial_paths):
    self._path_mod = path_mod
    self._initial_paths = set(initial_paths)
    self._paths = set()

  def _initialize(self):
    self._initialize = lambda: None
    for path in self._initial_paths:
      self.add(path)
    self._initial_paths = None
    self.contains = lambda path: path in self._paths

  def add(self, path):
    path = str(path)
    self._initialize()
    while path:
      self._paths.add(path)
      path = self._path_mod.dirname(path)

  def contains(self, path):
    self._initialize()
    return self.contains(path)


class fake_path(object):
  """Standin for os.path when we're in test mode.

  This class simulates the os.path interface exposed by PathApi, respecting the
  current platform according to the `platform` module. This allows us to
  simulate path functions according to the platform being tested, rather than
  the platform which is currently running.
  """

  def __init__(self, api, _mock_path_exists):
    self._api = api
    self._mock_path_exists = path_set(self, _mock_path_exists)
    self._pth = None

  def __getattr__(self, name):
    if not self._pth:
      if self._api.m.platform.is_win:
        import ntpath as pth
      elif self._api.m.platform.is_mac or self._api.m.platform.is_linux:
        import posixpath as pth
      self._pth = pth
    return getattr(self._pth, name)

  def mock_add_paths(self, path):
    """
    Adds a path and all of its parents to the set of existing paths.
    """
    self._mock_path_exists.add(path)

  def exists(self, path):  # pylint: disable=E0202
    """Return True if path refers to an existing path."""
    return self._mock_path_exists.contains(path)

  def abspath(self, path):
    """Returns the absolute version of path."""
    return self.normpath(path)

  def expanduser(self, path):
    return path.replace('~', '[HOME]')


def _split_path(path):  # pragma: no cover
  """Relative or absolute path -> tuple of components."""
  abs_path = os.path.abspath(path).split(os.path.sep)
  # Guarantee that the first element is an absolute drive or the posix root.
  if abs_path[0].endswith(':'):
    abs_path[0] += '\\'
  elif abs_path[0] == '':
    abs_path[0] = '/'
  else:
    assert False, 'Got unexpected path format: %r' % abs_path
  return abs_path


class PathApi(recipe_api.RecipeApi):
  """
  PathApi provides common os.path functions as well as convenience functions
  for generating absolute paths to things in a testable way.

  It defines paths to standard directories:
  - start_dir: the directory where the recipe execution starts.
  - cache: a directory where each subdirectory is a cache of a specific format,
    e.g. for git, isolate, goma, etc. A program that runs the recipe has a right
    to cleanup individual subdirectories in the cache directory.
    Typical usage: api.path["cache'].join("mycache")
  - tmp_base: the base directory for temporary files.

  Mocks:
    exists (list): Paths which should exist in the test case. Thes must be paths
      using the [*_ROOT] placeholders. ex. '[BUILD_ROOT]/scripts'.
  """

  OK_ATTRS = ('pardir', 'sep', 'pathsep')

  # Because the native 'path' type in python is a str, we filter the *args
  # of these methods to stringify them first (otherwise they would be getting
  # recipe_util_types.Path instances).
  FILTER_METHODS = ('abspath', 'basename', 'dirname', 'exists', 'expanduser',
                    'join', 'split', 'splitext')

  def get_config_defaults(self):
    return {
      'PLATFORM': self.m.platform.name,
      'START_DIR': self._startup_cwd,
      'TEMP_DIR': self._temp_dir,
      'CACHE_DIR': self._cache_dir,
    }

  def __init__(self, **kwargs):
    super(PathApi, self).__init__(**kwargs)
    config_types.Path.set_tostring_fn(
      PathToString(self, self._test_data))
    config_types.NamedBasePath.set_path_api(self)

    # Used in mkdtemp when generating and checking expectations.
    self._test_counter = 0

  def _read_path(self, property_name, default):  # pragma: no cover
    """Reads a path from a property. If absent, returns the default.

    Validates that the path is absolute.
    """
    props = self.m.properties.get('$recipe_engine/path', {})
    value = props.get(property_name)
    if not value:
      assert os.path.isabs(default), default
      return default
    if not os.path.isabs(value):
      raise Error(
        'Path "%s" specified by module property %s is not absolute' % (
          value, property_name))
    return value

  def initialize(self):
    if not self._test_data.enabled:  # pragma: no cover
      self._path_mod = os.path
      # Capture the cwd on process start to avoid shenanigans.
      self._startup_cwd = _split_path(os.getcwd())
      self._temp_dir = _split_path(
        self._read_path('temp_dir', tempfile.gettempdir()))
      self._cache_dir = _split_path(
        self._read_path('cache_dir', os.path.join(os.getcwd(), 'cache')))
    else:
      self._path_mod = fake_path(self, self._test_data.get('exists', []))
      self._startup_cwd = ['/', 'b', 'FakeTestingCWD']
      # Appended to placeholder '[TMP]' to get fake path in test.
      self._temp_dir = ['/']
      self._cache_dir = ['/', 'b', 'c']

    self.set_config('BASE')

  def mock_add_paths(self, path):
    """For testing purposes, assert that |path| exists."""
    if self._test_data.enabled:
      self._path_mod.mock_add_paths(path)

  def assert_absolute(self, path):
    assert self.abspath(path) == str(path), '%s is not absolute' % path

  def mkdtemp(self, prefix):
    """Makes a new temp directory, returns path to it."""
    if not self._test_data.enabled:  # pragma: no cover
      # New path as str.
      new_path = tempfile.mkdtemp(prefix=prefix, dir=str(self['tmp_base']))
      # Ensure it's under self._temp_dir, convert to Path.
      new_path = _split_path(new_path)
      assert new_path[:len(self._temp_dir)] == self._temp_dir
      temp_dir = self['tmp_base'].join(*new_path[len(self._temp_dir):])
    else:
      self._test_counter += 1
      assert isinstance(prefix, basestring)
      temp_dir = self['tmp_base'].join(
          '%s_tmp_%d' % (prefix, self._test_counter))
    self.mock_add_paths(temp_dir)
    return temp_dir

  def __contains__(self, pathname):
    return bool(self.c.dynamic_paths.get(pathname))

  def __setitem__(self, pathname, path):
    assert isinstance(path, config_types.Path), (
      'Setting dynamic path to something other than a Path: %r' % path)
    assert pathname in self.c.dynamic_paths, (
      'Must declare dynamic path (%r) in config before setting it.' % path)
    assert isinstance(path.base, config_types.BasePath), (
      'Dynamic path values must be based on a base_path' % path.base)
    self.c.dynamic_paths[pathname] = path

  def __getitem__(self, name):
    if name in self.c.base_paths or name in self.c.dynamic_paths:
      return config_types.Path(config_types.NamedBasePath(name))
    raise KeyError('Unknown path: %s' % name) # pragma: no cover

  def __getattr__(self, name):
    # retrieve os.path attributes
    if name in self.OK_ATTRS:
      return getattr(self._path_mod, name)
    if name in self.FILTER_METHODS:
      return string_filter(getattr(self._path_mod, name))
    raise AttributeError("'%s' object has no attribute '%s'" %
                         (self._path_mod, name))  # pragma: no cover

  def __dir__(self):  # pragma: no cover
    # Used for helping out show_me_the_modules.py
    return self.__dict__.keys() + list(self.OK_ATTRS + self.FILTER_METHODS)
