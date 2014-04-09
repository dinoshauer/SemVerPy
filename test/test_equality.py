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
