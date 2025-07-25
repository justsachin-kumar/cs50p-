def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

    if len(s)<2 or len(s)>6:
        return False
    #“All vanity plates must start with at least two letters.”
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if s[-1].isdigit() == True and s[-2].isalpha() == True:
        return False
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    i = 0
    while (i<len(s)):
        if s[i].isalpha() == False:
            if s[i] == '0' :
                return False

            else:
                break
        i += 1

#“No periods, spaces, or punctuation marks are allowed.”
    for char in s:
        if char in ["!", ".", " "]:
            return False

#passing right number palte
    else:
        return True

if __name__ == "__main__":
    main()
