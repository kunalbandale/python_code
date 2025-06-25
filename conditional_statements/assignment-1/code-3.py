# 3.wap to check the number is odd and check if the number is divisible by 7
# n=33
number = int(input("Enter Any Number:: "))

if number % 2 == 1:
    if number % 33 == 0:
        print(f"{number} is odd & divisble by 33")
else:
    print(f"{number} is even")

