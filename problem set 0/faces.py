def main():
    convert()


def convert():
    text = input().replace(":)", "🙂").replace(":(", "🙁")
    print(text)


main()
