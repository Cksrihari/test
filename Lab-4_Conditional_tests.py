#1
print(5 > 4)
print(6>7)
print(7<6)
print(10<11)
print(184371>3619)
print(101>2)
print(218946>83628736)
print(573753>6236836383)
print(2323>3232)
print(323>=323)
print("test"=="test")

#2
# a. Test using a lower() function.
a= "Correcr"
b= False
if a=="Correcrt":
    print("\n\nCorrect is present ")
    b=True
else:
    print("\n\nCorrect is not present ")
    b=False
print(b)
    

#3
b= input("\n\nDo you want to check the Day Number of any day(y/n): ")
while b=="y":
    a= input("Type the day(lowercase): ")
    if a=="monday":
        print(f"{a} is the 1st day of the week")
    elif a=="tuesday":
        print(f"{a} is the 2nd day of the week")
    elif a=="wednesday":
        print(f"{a} is the 3rd day of the week")
    elif a=="thursday":
        print(f"{a} is the 4th day of the week")
    elif a=="friday":
        print(f"{a} is the 5th day of the week")
    elif a=="saturday":
        print(f"{a} is the 6th day of the week")
    elif a=="sunday":
        print(f"{a} is the 7th day of the week")
    else:
        print("Please check your spelling\n")
    b= input("Do you want to try again?(y/n): ")

b= input("\n\nDo you want to check the number of days in a month(y/n): ")
while b=="y":
    a= input("Type the month(lowercase): ")  
    if a=="january":
        print(f"{a} has 31 days")
    elif a== "february":
        print(f"{a} has 28 or 29 days")
    elif a=="march":
        print(f"{a} has 31 days")
    elif a=="april":
        print(f"{a} has 30 days")
    elif a=="may":
        print(f"{a} has 30 days")
    elif a=="june":
        print(f"{a} has 31 days")
    elif a=="july":
        print(f"{a} has 30 days")
    elif a=="august":
        print(f"{a} has 31 days")
    elif a=="september":
        print(f"{a} has 30 days")
    elif a=="october":
        print(f"{a} has 31 days")
    elif a=="november":
        print(f"{a} has 30 days")
    elif a=="december":
        print(f"{a} has 31 days")
    else:
        print("please check your spelling")
    b= input("Do you want to try again(y/n): ")

#part-2
#1
a= input("\n\nWhat is your name?: ")
print(f"{a} is your name")

#2
a= input("Do you want to book a table?(y/n): ")
if a=="y":
    b= int(input("Table for how many?(numeric input): "))
    if b <= 8:
        print("Yor table is ready.\nThank you!")
    else:
        print("You may have to wait for a while to get a table.\nSorry for the inconvenience")
else:
    print("Ok!")

#3
a= int(input("Please enter a number: "))
if a%2==0:
    print("The entered number is a multiple of 2")
else:
    print("The entered number is not a multiple of 2")


#4
while True:
    try:
        age = input("Please enter your age: ")
        
        if age == -1:
            break  # Exit the loop if the user enters -1
        
        if age < 5:
            ticket_cost = 0
        elif 5 <= age <= 12:
            ticket_cost = 3
        elif age < 65:
            ticket_cost = 10
        else:
            ticket_cost = 5

        print(f"The ticket cost for a {age}-year-old is £{ticket_cost}")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
