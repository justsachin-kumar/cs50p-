def main():

    xy =  input("fraction: ")
    fraction = convert(xy)
    gar = gauge(fraction)
    print(f"{gar}")

def convert(ab):
    while True:
        try:
            a, b = ab.split("/")
            i=(int(a)/int(b))*100
            i=round(i)
            if i<=100 :
                return i
            else:
                ab =  input("fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(floated):

    z = floated
    if z == 99 or z==100 :
        return("F")
    elif z == 0 or z==1:
        return("E")
    else:

        return f"{z}%"




if __name__ =="__main__":
    main()
