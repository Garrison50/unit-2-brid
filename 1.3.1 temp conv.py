def main ():
    farenheit = int(input("What is the Farenheit temperature?"))
    celcius = (farenheit - 32) * 5/9
    print ("The temperature is", round(celcius, 1), "degrees Celcius!")

main()
