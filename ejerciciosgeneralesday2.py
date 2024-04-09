def numbers():
    number = int(input("Enter a number: "))

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


def tickets():
    amount_of_people = int(input("Enter the number of people: "))
    ticket_price = int(input("Enter the price of the ticket: "))
    estrate = int(input("Enter the estrate: "))
    age = int(input("Enter the age: "))

    total = amount_of_people * ticket_price

    for i in range(amount_of_people):
        if estrate == 1 and age < 18:
            discount = ticket_price - (ticket_price * 0.2)
        elif estrate == 1 and age >= 18:
            discount = ticket_price - (ticket_price * 0.15)
        elif estrate == 2 and age < 18:
            discount = ticket_price - (ticket_price * 0.1)
        else:
            discount = ticket_price - (ticket_price * 0.05)

    total_money_discount = discount * amount_of_people

    print(
        f"The total amount to recieved is:  { total}",
        "USD" + ".",
        f"The total amount to recieved with discount is:  { total_money_discount}",
        "USD",
        f"for {amount_of_people} people",
    )


def password():
    secret = "1234"

    for i in range(5):
        password = input("Enter your password: ")

        if password == secret:
            print("Access granted")
            break
        else:
            print("Access denied")
        if i == 2:
            print("You have reached the maximum number of attempts")
            break


def main():

    while True:
        print("1. Multiplication table")
        print("2. Tickets")
        print("3. Password")
        print("4. Exit")

        option = int(input("Enter an option: "))

        if option == 1:
            numbers()
        elif option == 2:
            tickets()
        elif option == 3:
            password()
        elif option == 4:
            break
        else:
            print("Invalid option")
        

main()

