# taking input from the user
text = input("Input:")
# creating a list containing all the vowels
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# apply a loop in vowel to check one by one and replce the value with the ""
for char in vowel:
    text = text.replace(char, "")
# printing the outputfor the user
print("Output:", text)
