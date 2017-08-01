def item_inventory(inventory, item):
    '''str -> str
    return item and price
    '''
    message = 'Sorry invalid item'
    for element in inventory:
        if item in inventory:
            return element[0:1] 
    return message

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
    message = 'invlaid item' 
    for item in inventory:
        if name in item:
            return item[4]
            