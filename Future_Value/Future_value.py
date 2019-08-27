def main():
    print ("Welcome to the interest calculator!")
    principal = 0
    print ("How much are you investing?")
    principal = float(input())
    if principal > 0:
        print ("Sounds good! $",principal, "is a smart amount to invest")
    elif principal == 0:
        print ("Sorry you have to invest at least a dollar!")
    else:
        print ("You can't invest negative money")
    print ("What's your yearly interest rate?")
    aprdec = float(input()) / 100
    print ("How many years are you calculating for?")
    years = int(input())
    count = 0
    if years >= 1:
        while count <= years:
            principal = principal * (1 + aprdec)
            count = count + 1
    print ("You'll have $", round(principal, 2), "after", years, "years!")
    repeat = (str(input("Would you like to try different values? (Yes or No)")))
    repeat = repeat.lower()
    if repeat == "yes":
        main()
    elif repeat == "no":
        print ("Hope this helped")
    else:
        print ("I can only work with the words 'yes' or 'no'")

main()