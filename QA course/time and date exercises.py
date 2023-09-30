# from datetime import datetime

#exersice 7.1:
# import datetime
# name = input("enter name: ")
# age = int(input("enter age: "))
# now = datetime.datetime.now()
# diffrence = 100 - age
# print(f"{name} you will turn 100 in {now.year + diffrence}")
# now = datetime.datetime.now()
# print(now)
# print(now.year,now.month,now.day)

#exercise 7.2:
# import datetime
# now = datetime.datetime.now()
# print("american:",now.month,"//",now.day,"//",now.year % 100)
# print(f"european: {now.day}//{now.month}//{now.year % 100}")

# exercise 7.3:
# from datetime import datetime
# date = input("enter date: ")
# date_object = datetime.strptime(date,"%b %d %Y")
# print(date_object)

#### external
# exercise 1:
# import time
# import datetime
# print("Current date and time: " , datetime.datetime.now())
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

# exercis 4
# from datetime import datetime
# now = datetime.now()
# time = now.time()
# print(time)

