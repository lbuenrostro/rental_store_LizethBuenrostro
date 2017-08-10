def load_inventory():
    ''' -> list[list]
    function return the products for rent
    '''
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    inventory = []
    for element in items:
        pieces = element.strip().split(', ')
        pieces[1] = float(pieces[1])
        pieces[2] = int(pieces[2])
        pieces[3] = float(pieces[3])
        inventory.append(pieces)
    return inventory


def load_history():
    '''  -> list[list]
    returns each piece in history'''
    with open('history.txt', 'r') as file:
        file.readline()
        items = file.readlines()
        inventory = []
        for item in items:
            pieces = item.strip().split(', ')
            inventory.append([
                pieces[0], pieces[1],
                int(pieces[2]),
                float(pieces[3]),
                float(pieces[4])
            ])
        return inventory


def update_history(name, item, hours, tax_price, deposit):
    ''' str, float, float -> None
    '''
    msg = name + ', ' + item + ', ' + str(hours) + ', ' + str(
        tax_price) + ', ' + str(deposit) + '\n'
    with open('history.txt', 'a') as file:
        file.write(msg)


def deposit_value(item):
    '''Float -> float'''
    message = '🎾Item not found🎾'
    with open('inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    for element in items:
        if item.title() in element:
            x = element.split(', ')
            depo = x[2]
            total = float(depo) * .10
            return '{:0.2f}'.format(total)
    return message
