
# taking mass as input in kg

def main():
    mass = int(input("mass(in kilograms):"))
    relativity(mass)


# defining relativity function
def relativity(n):
    c = 300000000
    e = n * (pow(c, 2))
    # printing output
    print(e)


main()
