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



def item_inventory(inventory, item):
    '''str -> str
    return item and price
    '''
    message = 'Sorry invalid item'
    for element in inventory:
        if item in inventory:
            return element[0:1] 
    return message