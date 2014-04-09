from semverpy import SemVerPy


def test_bump():
    v1 = SemVerPy('1.0.0')
    v1patch = SemVerPy('1.0.4')
    v1_1 = SemVerPy('1.1.0')
    v2 = SemVerPy('2.0.0')
    current = SemVerPy('1.0.0')
    assert current == v1
    [current.bump_patch() for i in range(4)]
    assert current == v1patch
    current.bump_minor()
    assert current == v1_1
    current.bump_major()
    assert current == v2
