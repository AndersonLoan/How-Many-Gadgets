# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ANDERSON WAYNE LOAN
# Section: 574
# Assignment: 4-8
# Date: 17/09/22
#

#sets values for function
#-2x - 1
gadgets = 0
b = 0
x = 1
day = 0
userDay = int(input("Please enter a positive value for day: "))
userO = userDay
def func (a, b): 
    a=a 
    
if userDay > 0:
    if userDay <= 10:
        gadgets = userDay * 5
    elif userDay <= 60:
        userDay = userDay - 10
        gadgets = 50 + (userDay * 50)
    elif userDay <= 100:
        if userDay == 61:
            userDay = userDay - 60
            gadgets = 2550 + (userDay * 50)
            gadgets = gadgets - x
        else:
            userDay = userDay - 60
            gadgets = 2550 + (userDay * 50)
            x = x + ((2*(userDay)))
            gadgets = gadgets - x
    print(f"The total number of gadgets produced on day {str(userO)} is {str(gadgets)}")
else:
    print("You entered an invalid number!")
print(x)
