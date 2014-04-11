from semverpy import SemVerPy, InvalidVersionException
from nose.tools import raises


@raises(InvalidVersionException)
def test_invalid():
    SemVerPy('1.a.0')
