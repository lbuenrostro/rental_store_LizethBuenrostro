def get_names(inventory):
    """ [[str, float, int, float]] -> [str]
    returns a list of the first items in a list of lists
    >>> get_names([['l', 'i', 'z', 'a'], ['bue', 'nro', 'st', 'ro']])
    ['l', 'bue']
    """
    names = []
    for item in inventory:
        names.append(item[0])
    return names


def tax_cost(money):
    ''' (float) -> float 
    This function will get the total_cost
    which will multiply *0.07 for every item
    >>> tax_cost(10.00)
    '10.07'
    >>> tax_cost(1.00)
    '1.07'
    >>> tax_cost(2.07)
    '2.14'
    '''
    tax = money * 0.07
    total = tax + money
    return '{:0.2f}'.format(total)


def return_deposit(inventory, name):
    ''' list[list], str -> float
    will return the return_deposit
    >>> return_deposit([['joy', 'tennis balls', '6', '160.50', '10.00']], 'joy')
    10.00
    >>> return_deposit([['jake', 'Pro Tennis Black Bag', '4', '64.20', '4.50']], 'jake')
    4.50
    >>> return_deposit([['elisa', 'tennis black shoes', '4', '64.20', '6.50']], 'elisa')
    6.50
    '''
    message = 'invalid item'
    for item in inventory:
        if name in item:
            return item[4]
    return message


def total_deposits(history):
    ''' list[list] -> float
    calculate total revenue 
    to user 
    the rental purchase is index 3
    and the deposit value is index 4
    '''
    x = 0
    for item in history:
        x += item[3] + item[4]
    return x


def total_money(item, hours, amount, inventory):
    '''Float, float, float, [[]] -> float'''
    for element in inventory:
        if item == element[0]:
            rate = float(element[1])
            total = rate * float(hours) * float(amount)
            return total
    return '🎾Item not found🎾'