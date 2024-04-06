# defining main


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # calculating tip
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# defining dollar to float function


def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return d


# defining tip function


def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p) * (1 / 100)
    return p


# calling main

main()
