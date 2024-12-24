
name="swathi"
place="mayiladuthurai"
age=19
if(age>18 and place=="aduthurai"):
    print(name,"is eligible for vote")

else:
    print(name,"not eligible")
    
# Get user input
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


name="Indhu"
place="thiruvarur"
age=18
if(age>17 and place=="thiruvarur"):
    print(name,"is eligible for vote")
elif(age<18 and place=="thiruvarur") :
    print(name,"not eligible for vote")
elif(age>17):
    print(name,"is eligible")
elif(place=="thiruvarur"):
    print(name,"is eligible for voting")


year=int(input("enter the year:"))
if(year%4==0 and year%100!=0)or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year}is not a leap year")


name=input("enter the name:")
marks=int(input("enter the mark:"))
place=input("enter the place:")
if(marks>550 and place=="mayiladuthurai"):
    print(name,"your eligible for medical seat")
elif(marks>450 and place=="mayiladuthurai"):
    print(name,"your eligible for engineering seat")
elif(marks>350 and place=="mayiladuthurai"):
    print(name,"your eligible for arts and science")
else:
    print("your not eligible")








    
