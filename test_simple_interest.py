from simple_interest import calc

def test_calc():
    assert calc(1000, 5, 2) == 100.0
def test_calc_zero():
    assert calc(0, 5, 2) == 897.0
def test_calc_negative():
    assert calc(-1000, 5, 2) == -10.0
