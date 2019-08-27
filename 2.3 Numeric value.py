def main():
    count = int(input("How many words are you entering?"))
    time = 0
    self = "Your acronym is: "
    while count > time:
        word = str(input("Enter the word"))
        acr = word.title()
        time = time + 1
        self = self + acr[0]
    print (self)
main()