import core


def test_tax_cost():
    money = core.tax_cost(10.00)
    expected = '10.70'
    assert money == expected

def test_return_deposit():
    actual = core.return_deposit(
        [['bob', 'Pro Tennis Black Bag', 4, 64.20, 7.50]], 'bob')
    expect = 7.50
    assert expect == actual
    actual = core.return_deposit(
        [['bob', 'Pro Tennis Black Bag', 4, 64.20, 7.50]], 'billy')
    expect = 'invalid item'
    assert expect == actual

def total_deposits():
