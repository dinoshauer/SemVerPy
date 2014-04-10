import re

__version__ = '0.0.1'
__author__ = 'Kasper Jacobsen'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Kasper Jacobsen'


class InvalidVersionException(Exception):
    pass


class SemVerPy():
    def __init__(self, version):
        self.pattern = r'(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(?:-(?P<build>\w*)|)'
        version = self._validate(version)
        self._major = version['major']
        self._minor = version['minor']
        self._patch = version['patch']
        self._build = version['build']

    def __str__(self):
        if self.version['build'] is not None:
            return '{major}.{minor}.{patch}-{build}'.format(
                self._major,
                self._minor,
                self._patch,
                self._build,
            )
        return '{major}.{minor}.{patch}'.format(
            self._major,
            self._minor,
            self._patch,
        )

    def __repr__(self):
        return '<{}({})>'.format(
            self.__class__.__name__, str(self)
        )

    def __getitem__(self, key):
        return self.version[key]

    def __setitem__(self, key, value):
        self.version[key] = value
        return self.version

    def _tuple(self):
        major = self.version['major']
        minor = self.version['minor']
        patch = self.version['patch']
        build = self.version['build']

        return major, minor, patch, build

    def __eq__(self, other):
        if not isinstance(other, SemVerPy):
            return False
        else:
            return self._tuple() == other._tuple()

    def __ne__(self, other):
        return not self == other

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
        return re.search(self.pattern, string).groupdict()

    @staticmethod
    def _parse_dict(version_dict):
        try:
            version_dict['major'] = int(version_dict['major'])
            version_dict['minor'] = int(version_dict['minor'])
            version_dict['patch'] = int(version_dict['patch'])
            return version_dict
        except ValueError:
            raise

    def _validate(self, string):
        try:
            version = self._get_dict(string)
            version_dict = self._parse_dict(version)
            return version_dict
        except AttributeError:
            raise InvalidVersionException('Not a valid version: {}'.format(string))

    def bump_major(self, build=None):
        self._major += 1
        self._minor = 0
        self._patch = 0
        self._build = build
        return self.version

    def bump_minor(self, build=None):
        self._minor += 1
        self._patch = 0
        self._build = build
        return self.version

    def bump_patch(self, build=None):
        self._patch += 1
        self._build = build
        return self.version

    def set_build(self, build_string):
        self.version['build'] = build_string
        return self.version
