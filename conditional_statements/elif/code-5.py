# wap to take marks of 5 subjects , cal the avg
# if avg is b/w 90-100 print distinction
# if 75-89 print first class and
# if its 60-74 print second class , if 50-59 print Third class below 50 fail

# note : max marks 100

subject1 = int(input("Enter the Marks for Subject 1 (0-100)"))
subject2 = int(input("Enter the Marks for Subject 2 (0-100)"))
subject3 = int(input("Enter the Marks for Subject 3 (0-100)"))
subject4 = int(input("Enter the Marks for Subject 4 (0-100)"))
subject5 = int(input("Enter the Marks for Subject 5 (0-100)"))

totalMarks = (subject1 + subject2 + subject3 + subject4 + subject5)
avgMarks = (totalMarks / 5)
per = (totalMarks / 500) * 100

# print(avgMarks)

if 90<=avgMarks<=100:
    print("Distinction")
elif 75<=avgMarks<=89:
    print("First Class Pass")
elif 60<=avgMarks<=74:
    print("Second Class Pass")
elif 50<=avgMarks<=59:
    print("Third Class Pass")
else:
    print("Fail")

print("Your Percentage : " , per)