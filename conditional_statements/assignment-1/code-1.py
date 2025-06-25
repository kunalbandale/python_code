# 1.wap to check whether the given number is even and greater than 5
# num=2

number = int(input("Enter Any Number:: "))

if number % 2 == 0:
    if number > 5:
        print(f"{number} is even & greater than 5")
else:
    print(f"{number} is odd")

