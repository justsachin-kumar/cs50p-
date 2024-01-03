def main():

    say_word(input("what do you wanna say? "))

def say_word(name):
    for i in range(int(input("how many times? "))):
        print(f"{i+1}.",name)
    
        
        
main()