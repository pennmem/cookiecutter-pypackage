from collections import namedtuple

__version__ = '{{ cookiecutter.version }}'
version_info = namedtuple("VersionInfo", "major,minor,patch")(*__version__.split('.'))
