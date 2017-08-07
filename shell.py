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
def rent_store():
    slow_type('\n             🎾WELCOME to Tennis Rental Agency🎾.Press Enter...             \n')
    slow_type('🎾Rental Agency charges by Hour🎾\n🎾Deposit is 10% of every item🎾\n🎾We do not sale. Only Rent🎾\n')   
    inventory = disk.load_inventory()
    print(inventory)
    item = slow_type('What type of equipment would you like?\t').title().strip()
    hours = slow_type('How many hours would you like to rent it for?\t').strip()
    amount = slow_type('How many would you like?\t').strip()
    answer = disk.total_money(item, float(hours), amount)
    tax = core.tax_cost(float(answer))
    print('Your total is $', tax)
    deposit = disk.deposit_value(item)
    print('Deposit is $', deposit)
    name = slow_type('What is your name?\n').title().strip()
    disk.update_history(name, item, hours, tax, deposit)      
    print('🎾Thanks for stopping by, come back SOON!!🎾') 
def main():
    choice = slow_type('🎾If you wish to look at the store PRESS s🎾\n🎾If you want to return an item PRESS r🎾\n🎾Manager check PRESS m🎾\n')
    if choice.lower() == 's':
        rent_store()
    elif choice.lower() == 'r':
        items = disk.load_items()
        name = slow_type('What is your name?\n').title().strip()
        all_invi = disk.load_items()
        return_depo = core.return_deposit(all_invi, name) 
        print('Here is your deposit $', return_depo) 
if __name__ == '__main__':
    main()