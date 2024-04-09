

def translate_numbers(number):
    

    number = "-".join(number)


    number = number.replace("1", "one")
    number = number.replace("2", "two")
    number = number.replace("3", "three")
    number = number.replace("4", "four")
    number = number.replace("5", "five")
    number = number.replace("6", "six")
    number = number.replace("7", "seven")
    number = number.replace("8", "eight")
    number = number.replace("9", "nine")
    number = number.replace("0", "zero")


    return number

num_to_translate =  input("Enter a number: ")


print(translate_numbers(num_to_translate ))













   



    










    


