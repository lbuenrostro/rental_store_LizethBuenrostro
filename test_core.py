import core 

def test_tax_cost():
    money = core.tax_cost(10.00)
    expected = '10.70'
    assert money == expected

def test_item_inventory():
    actual = core.item_inventory([['bob', 25, 4.00]], 'bob')
    expect = 4.00
    assert expect

def test_return_deposit(): 
    actual = core.return_deposit([['bob', 'Pro Tennis Black Bag', 4, 64.20, 7.50]], 'bob')
    expect = [['bob', 'Pro Tennis Black Bag', 4, 64.20, 7.50]]
    assert expect

