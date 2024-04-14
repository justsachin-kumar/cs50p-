#create a list with the name of all months
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#loop forever
while True:
    #get user input
    anno_domini: str = input("Dates: ")
    #split the date by "/"
    try:
        month, day, year = anno_domini.split("/")
        #check if month is btw 1-12 and day is 1-31
        if (int(month) >= 1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
            break
    #split the date by space
    except:
        try:
            month, day, year = anno_domini.strip().split(" ")
            #find the number of month:

            for i in range(len(month_list)):
                if month == month_list[i]:
                    month = i+1
            #remove comman from the day varibale
            if "," in day:
                day = day.strip(",")
            else:
                raise ValueError


            #check if the month is in btw 1-12 and day 1-31
            if (int(month) >= 1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
                break
#go to the next line
        except ValueError:
            pass
#if month or day less then 10 add zero befor

#print the user output
print(f"{int(year)}-{int(month):02}-{int(day):02}", end = "")
