        
def main():   
    
    x=int(input("hight of the pyramid ? "))
    print_pyramid(x)
    
    
    
def natural_number():
    for i in range(0,20):
        return i
n= natural_number()
    
#n= list(range(50))

def print_pyramid(a):
    for n in range(a):
        print("*" * (2*n+1))

main()
    
    
