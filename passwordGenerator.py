import random

small_characters = 'abcdefghijklmnopqrstuvwxyz'
capital_characters = small_characters.upper()
special_characters = "-*/+._"
numbers = "0123456789"
length = 0


program = True

print("_______________________________________________")
print("           Strong Password Generator")


while program:
    entry = input("""
        Choose your preferences for a password.
        [0] - Exit
        [1] - Numbers Only
        [2] - Capital Letters Only
        [3] - Small Letters Only
        [4] - Numbers + Capital Letters
        [5] - Numbers + Small Letters
        [6] - Numbers + Special Characters
        [7] - A mix of all
        [Answer] : """)
    length = int(input("        What should be the length of your password? "))
    if entry == '0':
        print("             Program Closed")
        program = False

    if entry == '1':
        password = "".join(random.sample(numbers, length))
        print(f"        Password Generated: {password}")

    elif entry == '2':
        password = "".join(random.sample(capital_characters, length))
        print(f"        Password Generated: {password}")

    elif entry == '3':
        password = "".join(random.sample(small_characters, length))
        print(f"        Password Generated: {password}")
    
    elif entry == '4':
        password = "".join(random.sample(numbers + capital_characters, length))
        print(f"        Password Generated: {password}")
    
    elif entry == '5':
        password = "".join(random.sample(numbers + small_characters, length))
        print(f"        Password Generated: {password}")
    
    elif entry == '6':
        password = "".join(random.sample(numbers + special_characters, length))
        print(f"        Password Generated: {password}")
    
    elif entry == '7':
        password = "".join(random.sample(numbers + special_characters + capital_characters + small_characters, length))
        print(f"        Password Generated: {password}")

    keepRunning = input("       Do you want to close the program? ")
    if keepRunning == 'yes':
        print("             Program Closed")
        program = False