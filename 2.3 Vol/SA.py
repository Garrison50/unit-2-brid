def main():
    import math
    radius = float(input("Enter the radius of the sphere"))
    volume =  ((4/3) * math.pi * (pow(radius,3)))
    sa = (4 * math.pi * (pow(radius,2)))
    print ("The volume is:", round(volume,2))
    print ("The surface area is:", round(sa,2))
main()