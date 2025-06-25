# wap to check a age belongs to category
# 0 to 17 child and 18 to 30 ur adult , 31 to 60 ur men , 61 to 100 senior citizen else invalid

age = eval(input("Enter Your Age"))

if age >= 0 and age <= 17:
    print("Child")
elif age >= 18 and age <= 30:
    print("Adult")
elif age >= 31 and age <= 60:
    print("Men")
elif age >= 61 and age <= 100:
    print("Senior Citizen")
else:
    print("Enter Valid Age")