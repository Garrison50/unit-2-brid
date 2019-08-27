def main():
    count = int(input("How many numbers would you like to add?"))
    number = 0
    value = 0
    while count > number:
        number = number + 1
        choice = float(input("What number would you like to add?"))
        value = value + choice
    print ("The grand total is:", value)
main()