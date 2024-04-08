# declare amount due

amount = 50
# apply a loop to accept only valid denomination
while amount > 0:
    # printing amount due
    print(
        f"Amount Due: {amount}",
    )
    # accepting a coin
    x = int(input("Insert Coin: "))
    # checking if the coin is valid or not
    if x == 25 or x == 10 or x == 5:
        amount = amount - x
# condition if the owned change is negative
amount = abs(amount)
# printing owned change
print(
    f"Change Owed: {amount}",
)
