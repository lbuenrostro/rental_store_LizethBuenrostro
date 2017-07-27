def update_history(item, price, items_left):
    ''' str, float, float _> None
    '''
    msg = item + ', ' + str(price) + ', ' + str(items_left) + '\n'
    with open('history.txt', 'a') as file:
        file.write(msg)

def load_inventory():
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    inventory = []
    for element in items:
        pieces = element.split(', ')
        inventory.append([pieces[0]])
    return inventory

def function_total(amount, item, days):
    '''Float, float, float -> float'''
    message = '🏸Item not found🏸'
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    for element in items:
        if item.title() in element:
            pieces = element.split(', ')
            price = float(pieces[1]) 
            total = price * amount * days
            return total 
    return message

def price_of(item_name):
    ''' ([[str, float, float]], str) -> (float)
    This function will get a string and 
    it will look in a txt file and pull out 
    the price of the item and return it
    '''
    message = 'item not found in rental'
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    for element in items:
        if item_name in element:
            pieces = element.split(', ')
            price = pieces[1] 
            return price
    return message
