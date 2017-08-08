import core
import disk


def rent_store():
    input(
        '\n             🎾WELCOME to Tennis Rental Agency🎾.Press Enter...             \n'
    )
    input(
        '🎾Rental Agency charges by Hour🎾\n🎾Deposit is 10% of every item🎾\n🎾We do not sale. Only Rent🎾\n'
    )
    inventory = disk.load_inventory()
    print(inventory)
    item = input('What type of equipment would you like?\t').title().strip()
    hours = input('How many hours would you like to rent it for?\t').strip()
    amount = input('How many would you like?\t').strip()
    answer = disk.total_money(item, float(hours), amount)
    tax = core.tax_cost(float(answer))
    print('Your total is $', tax)
    deposit = disk.deposit_value(item)
    print('Deposit is $', deposit)
    name = input('What is your name?\n').title().strip()
    disk.update_history(name, item, hours, tax, deposit)
    print('🎾Thanks for stopping by, come back SOON!!🎾')


def manager_check():
    welcome = input('\nWelcome Manager...\n')
    user = 'manager'
    password = "tennis_90"
    username = input("Please enter username: ")
    pw = input("Please enter password: ")
    if username in user and pw == password:
        print(
            input(
                'Welcome Mr. ' + username +
                ' 🎾WELCOME to Tennis Rental Agency🎾:display total revenue\n\n... Press ENTER to continue...\n'
            ))
    else:
        print('Invalid Username')
        exit()
    items = disk.load_items()
    print(items)


def main():
    choice = input(
        '🎾If you wish to look at the store PRESS s🎾\n🎾If you want to return an item PRESS r🎾\n🎾Manager check PRESS m🎾\n'
    )
    if choice.lower() == 's':
        rent_store()
    elif choice.lower() == 'm':
        manager_check()
    elif choice.lower() == 'r':
        items = disk.load_items()
        name = input('What is your name?\n').title().strip()
        all_invi = disk.load_items()
        return_depo = core.return_deposit(all_invi, name)
        print('Here is your deposit $', return_depo)


if __name__ == '__main__':
    main()