# 4. **WAP to check** whether two input numbers are divisible by both 3 and 5.
# If divisible, print “Good Morning”; otherwise, print “Good Evening.”

number_1 = int(input("Enter Any Number-1  "))
number_2 = int(input("Enter Any Number-2  "))

if number_1 % 3 == 0 and number_1 % 5 == 0:
    if number_2 % 3 == 0 and number_2 % 5 == 0:
        print("Good Morning")
    else:
        print("Good Evening")
else:
    print("Good Evening")



