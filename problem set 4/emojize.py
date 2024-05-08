import emoji


text = input("Input: ")
try:
    emojize = emoji.emojize(text)
    print(f"Output: {emojize}")
except:
    pass
else:
    emojize = emoji.emojize(text, language="alias")
    print(f"Output: {emojize}")
