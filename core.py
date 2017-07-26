def total_cost(item_price):
    """ (float) -> float 
    This function will get the total_cost
    which will multiply *0.07 for every item
    >>> total_cost(1.00)
    1.07
    >>> total_cost(5.00)
    5.07 
    >>> total_cost(4.00)
    4.07 
    """
    item = item_price * 0.07
    result = item_price + item
    return "%.2f" % result 

