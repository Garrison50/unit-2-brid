def main():
    quiz = float(input("Enter the quiz score:"))
    if quiz >= 90 and quiz <= 100:
        print ("A")
    elif quiz >= 80 and quiz <= 89:
        print ("B")
    elif quiz >= 70 and quiz <= 79:
        print ("C")
    elif quiz >= 60 and quiz <= 69:
        print ("D")
    else:
        print ("F")
    redo = int(input("Would you like to endter more scores? 1 - yes, 2 - no"))
    if redo == 1:
        main()
    else:
        print("Hope this helped!")
main()