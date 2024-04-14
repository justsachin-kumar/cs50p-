grocery_list = []
grocery_counts = {}
while True:
    try:
        item = input().upper()
        grocery_list.append(item)
        grocery_list.sort()

    except EOFError:
        for grocery in grocery_list:
            if grocery in grocery_counts:
                grocery_counts[grocery] += 1
            else:
                grocery_counts[grocery] = 1
        sorted(grocery_list)
        for grocery, count in grocery_counts.items():

            print( f"{count} {grocery}")



        exit()



#
