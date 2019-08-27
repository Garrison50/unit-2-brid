def main():
    number = 2
    dividend = 2
    count = 0
    for number in range(2,100):
        if number % dividend == 0:
            count = count + 1
            break
        else:
            print (number, "is a prime number!")

main()
