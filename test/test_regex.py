from semverpy import SemVerPy, InvalidVersionException
from nose.tools import raises


@raises(InvalidVersionException)
def test_invalid():
    SemVerPy('1.a.0')


def test_regex():
    SemVerPy('v1.0.0')
    SemVerPy('V1.0.0')

    SemVerPy('v1.0.0-build')
    SemVerPy('V1.0.0-build')

    SemVerPy('v1.0.0+build')
    SemVerPy('v1.0.0:build')


@raises(InvalidVersionException)
def test_invalid_build():
    SemVerPy('v1.0.0-build info')


@raises(InvalidVersionException)
def test_invalid_separators():
    SemVerPy('1-0-0')


def test_partial_version():
    SemVerPy('1.1')


def test_dependency():
    SemVerPy('1.2.x', dependency=True)
