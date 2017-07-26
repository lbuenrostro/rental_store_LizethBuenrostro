def update_inventory(item, price, items_left):
    ''' str, float, float _> None
    '''
    msg = item + ', ' + str(price) + ', ' + str(items_left) + '\n'
    with open('history.txt', 'a') as file:
        file.write(msg)