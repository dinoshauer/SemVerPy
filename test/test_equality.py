from semverpy import SemVerPy


def test_same():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.1-a')
    assert v1 == v2


def test_not_same():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.1-a')
    assert not v1 != v2
    v3 = SemVerPy('0.0.2-a')
    assert v1 != v3


def test_less_than():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.3-a')
    assert v1 < v2


def test_greater_than():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.3-a')
    assert v2 > v1


def test_less_equal():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.3-a')
    assert v1 <= v2


def test_greater_equal():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.3-a')
    assert v2 >= v1


def test_fails():
    v1 = SemVerPy('0.0.1-a')
    v2 = SemVerPy('0.0.1-a')
    assert not v2 > v1
    assert not v2 < v1

    v1 = SemVerPy('1.1.0')
    v2 = SemVerPy('2.0.0')
    assert v1 != v2
    assert not v1 > v2
    assert v1 < v2


def test_dependency_matches():
    dependency = SemVerPy('2.3')
    version = SemVerPy('2.3.5-finalfinallast')
    assert dependency == version
    assert version != dependency
    assert version > dependency
    assert not version < dependency
