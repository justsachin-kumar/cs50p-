def main():
    cal = input("Expression: ")
    interpreter(cal)


def interpreter(cal):
    x, y, z = cal.split(" ")
    x = float(x)
    z = float(z)
    # calculation for actual math

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        print(x / z)


main()
