def main():
    import math
    radius = float(input("Enter the diameter of the pizza (in inches)")) / 2
    price = float(input("Enter the price of the pizza"))
    area = (math.pi * pow(radius, 2))
    value = price / area
    print("This pizza is worth $", round(value, 2), "per sq in")
main()