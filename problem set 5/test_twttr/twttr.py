def main():

    test = input("Input:")
    striped_word  = shorten(test)
    print(f"Output: {striped_word}")

def shorten(word):
    #taking input from the user
    #creating a list containing all the vowels
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    #apply a loop in vowel to check one by one and replce the value with the ""
    for char in vowel:
        word = word.replace(char, "")
    #printing the outputfor the user
    return word


if __name__ == "__main__":
    main()
