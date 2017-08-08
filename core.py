def tax_cost(money):
    ''' (float) -> float 
    This function will get the total_cost
    which will multiply *0.07 for every item
    '''
    tax = money * 0.07
    total = tax + money
    return '{:0.2f}'.format(total)


def return_deposit(inventory, name):
    ''' list[list], str -> float
    will return the return_deposit
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
    '''
    x = 0
    for item in history:
        x += item[4]
    return x
