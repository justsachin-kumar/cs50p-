# import inflect package(https://pypi.org/project/inflect/)
import inflect

p = inflect.engine()
# make a list that will contain all names
name_list: list[str] = []

# apply a loop that prompt user for name and raise an exception when pressed (ctrl+d)
while True:
    try:
        name = input("name: ")
        name_list.append(name)

    except EOFError:
        new_list = p.join(name_list)
        break

# join names into a list and add them into a new list and print user output
print("Adieu, adieu, to", new_list)
