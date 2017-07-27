import core
import disk
import time 
import sys
typing_speed = 25
def slow_type(t):
    for l in t:
        sys.stdout.write(l) 
        sys.stdout.flush() 
        time.sleep(typing_speed / 970.0)
    return input()

def main():
    slow_type('\n🏸WELCOME to Tennis Rental Agency🏸.Press Enter... \n')
    item = slow_type("what would you like today?🏸\n")
    inventory = disk.load_inventory()
    print(inventory)
    item = slow_type("What type of equipment would you like?\t").title().strip()
    price = core.price_of(inventory, item) 
    print(price)    

    # update_inventory(item, price, items_left)      
    print('🏸Thanks for stopping by, come back SOON!!🏸') 
if __name__ == '__main__':
    main()