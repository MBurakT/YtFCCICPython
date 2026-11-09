try:
    number = int(input("How old are you? "))
    print(number)
except ValueError as ver:
    print("Please enter a number")
