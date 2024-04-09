def translate_numbers(number):
    list = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }
    number = "-".join(number)
    for i in number:

        if i in list:

            number = number.replace(i, list[i])

    return number


num_to_translate = input("Enter a number: ")


print(translate_numbers(num_to_translate))
