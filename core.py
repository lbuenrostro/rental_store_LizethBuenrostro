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
    return '{:0.2f}'.format(result)


# def deposit_refund(item_replace):
#     """ (float) -> float 
#     This function will get the deposit_refund
#     which will multiply *0.10 for every item
#     >>> deposit_refund(2.00)
#     2.10
#     >>> deposit_refund(1.00)
#     1.10
#     >>> deposit_refund(3.00)
#     3.10
#     """
#     item = item_replace * 0.10
#     result = item_replace + item
#     return '{:0.2f}' % result 

def price_of(inventory, item_name):
    ''' ([[str, float, float]], str) -> (float)
    This function will get a string and 
    it will look in a txt file and pull out 
    the price of the item and return it
    ''' 
    message = 'Sorry invalid item'
    store = []
    for item in inventory:
        pieces = item.split(', ')
        if item_name.title() in item:
            return float(pieces[1])
    return message

def item_inventory(inventory, item):
    '''str -> str
    return item and price
    '''
    message = 'Sorry invalid item'
    for element in inventory:
        if item in inventory:
            return element[0:1] 
    return message

def function_total(amount, item, days):
    '''Float, float, float -> float'''
    
