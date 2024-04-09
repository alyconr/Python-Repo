def items():
    amount_of_items = int(input("Enter the amount of items: "))

    list_of_items = []

    for i in range(amount_of_items):
        item1 = input("Enter the item:  ")

        list_of_items.append(item1)

    print("Original list: ", list_of_items)
    # reverse list:
    list_of_items.reverse()
    print("Reversed list: ", list_of_items)

def delete_number():
    list_of_disorder_numbers = ['2', '4', '6', '8', '10', '1', '3', '5', '7', '9', '10', '6']

    get_number = int(input("Enter a number: "))

    for i in list_of_disorder_numbers:
        if get_number == int(i):   
        
            list_of_disorder_numbers.remove(i)

    print(list_of_disorder_numbers)



def phrases():
    phrase1 = input("Enter a phrase: ")
    phrase2 = input("Enter another phrase: ")
    result_list = []

    for i in phrase1 :
        if i in phrase2:
            result_list.append(i)

    print(result_list)

def main():
    
    while True:
        print("1. Items")
        print("2. Delete number")
        print("3. Phrases")
        print("4. Exit")

        option = int(input("Enter an option: "))

        if option == 1:
            items()
        elif option == 2:
            delete_number()
        elif option == 3:
            phrases()
        elif option == 4:
            break
        else:
            print("Invalid option")


main()
