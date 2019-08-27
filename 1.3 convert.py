def main ():
    count = 0
    while count <= 5:
        celcius = eval(input("What is the Celcius temperature?"))
        farenheit =9/5 * celcius + 32
        print ("The temperature is", round(farenheit, 1), "degrees Farenheit!")
        count = count + 1
main()
