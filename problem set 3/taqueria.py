menu = {"Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}

total_amount = 0.00

while True:
    try:
        item = input("item:").title()
        if item in menu:
            total_amount += menu[item]
            print(f"total: ${total_amount:.2f}")
    except EOFError:

        exit()



