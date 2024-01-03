def main():
    s=int(input("what's the side of a square?"))
    print_square(s)
    
    
def print_square(x):
    for i in range(x):
        print("# " * x)
        
        
        
main()