def main():
    unit = int(input("How many full units have you completed?"))
    assign = int(input("How many assignments have you done in your current unit?"))
    totunit = 6
    totassign = 30
    unitper = unit / totunit
    totprog = (unitper + assign/totassign)
    print ("You're", round((totprog*100),2), "% completed with this course")
main()