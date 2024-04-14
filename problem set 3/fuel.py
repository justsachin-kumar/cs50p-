def main():
    z = fuel()
    if z == 99 or z==100 :
        print("F")
    elif z == 0 or z==1:
        print("E")
    else:

        print (f"{z}%")
def fuel():

    while True:
        try:
            x, y =  input("fraction: ").split("/")

            i=(int(x)/int(y))*100
            i=round(i)
            if i>100:
                raise ValueError
            return i


        except (ValueError, ZeroDivisionError,):
            pass
        else:
            break






main()
