from semverpy import SemVerPy


def test_same():
    ver = SemVerPy('1.0.1-a')
    print(str(ver))
    assert str(ver) == '1.0.1-a'


def test_dependency():
    ver = SemVerPy('1.2')
    print(str(ver))
    assert str(ver) == '1.2.x'
