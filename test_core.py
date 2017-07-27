import core 

def test_total_cost():
    assert core.total_cost(1.00) == 1.07
    assert core.total_cost(5.00) == 5.07 
    assert core.total_cost(4.00) == 4.07 
 


def test_deposit_refund():
    assert core.deposit_refund(2.00) == 2.10
    assert core.deposit_refund(1.00) == 1.10
    assert core.deposit_refund(3.00) == 3.10

