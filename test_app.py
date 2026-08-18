from app import suma, resta


def test_suma():
    assert suma(5, 3) == 8


def test_resta():
    assert resta(5, 3) == 2