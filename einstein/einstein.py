def main():
    mass=int(input("mass(in kilograms):"))
    relativity(mass)
    
def relativity(n):
    c=300000000
    e=n*(pow(c,2))
    print(e)
    
main()
