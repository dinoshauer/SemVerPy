import re

__version__ = '0.0.1'
__author__ = 'Kasper Jacobsen'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Kasper Jacobsen'

_start = r'^v?'
_major = r'(?P<major>\d+)'
_minor = r'(\.(?P<minor>\d+))?'
_patch = r'(\.(?P<patch>\d+))?'
_build = r'(?:[:+-](?P<build>\w+))?'
_end = r'$'

_regex = _start + _major + _minor + _patch + _build + _end
# _regex = r'^v?(?P<major>\d+)(\.(?P<minor>\d+))?(\.(?P<patch>\d+))?(?:[:+-](?P<build>\w+))?$'


class InvalidVersionException(Exception):
    pass


class SemVerPy():
    _pattern = re.compile(_regex, re.IGNORECASE)

    def __init__(self, version):
        version = self._parse(version)
        self._major = version['major']
        self._minor = version['minor']
        self._patch = version['patch']
        self._build = version['build']

    def __str__(self):
        res = '{major}.{minor}.{patch}'.format(
            major=self._major,
            minor=self._minor,
            patch=self._patch,
        )

        if self._build:
            res += '-{}'.format(self._build)
        return res

    def __repr__(self):
        return '<{name}({info})>'.format(
            name=self.__class__.__name__,
            info=str(self),
        )

    def _tuple(self):
        return self._major, self._minor, self._patch, self._build

    def satisfies(self, item):
        for s, o in zip(self._tuple(), item._tuple()):
            if o is not None and s != o:
                return False
        return True

    def __eq__(self, other):
        if not isinstance(other, SemVerPy):
            return False
        else:
            return self._tuple() == other._tuple()

    def __ne__(self, other):
        return self._tuple() != other._tuple()

    def __lt__(self, other):
        if not isinstance(other, SemVerPy):
            return False
        else:
            return self._tuple() < other._tuple()

    def __gt__(self, other):
        if not isinstance(other, SemVerPy):
            return False
        else:
            return self._tuple() > other._tuple()

    def __le__(self, other):
        return self._tuple() <= other._tuple()

    def __ge__(self, other):
        return self._tuple() >= other._tuple()

    def _get_dict(self, string):
        return self._pattern.search(string).groupdict()

    def _parse(self, version_string):
        res = self._pattern.search(version_string)
        if res is None:
            msg = 'Not a valid version: {}'.format(version_string)
            raise InvalidVersionException(msg)
        else:
            return self._convert_fields(res.groupdict())

    def _convert_fields(self, version_dict):
        for key in ['major', 'minor', 'patch']:
            try:
                version_dict[key] = int(version_dict[key])
            except TypeError:
                pass
        return version_dict

    def bump_major(self, build=None):
        self._major += 1
        self._minor = 0
        self._patch = 0
        self._build = build
        return self

    def bump_minor(self, build=None):
        self._minor += 1
        self._patch = 0
        self._build = build
        return self

    def bump_patch(self, build=None):
        self._patch += 1
        self._build = build
        return self

    def set_build(self, build_string):
        self._build = build_string
        return self
