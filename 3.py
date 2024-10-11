inventory_list = []


def add_item(item):
    inventory_list.append(item)


def remove_item(item):
    inventory_list.remove(item)


def show_inventory():
    print(inventory_list)


def main():
    while True:
        prompt = input('Enter \'add\' to add item or \'remove\' to remove item or \'show\' to show items or \'exit\' to exit from program: ')

        if prompt == 'add':
            item = input('Enter a name of item: ')
            add_item(item)
            show_inventory()
        elif prompt == 'remove':
            item = input('Enter a name of item: ')
            remove_item(item)
            show_inventory()
        elif prompt == 'show':
            show_inventory()
        elif prompt == 'exit':
            break


main()
