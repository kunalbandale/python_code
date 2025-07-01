# 6.wap to print the count of alphabets and numbers and space in the given string
# s="india got the independence in the year 1947"

space = 0
number = 0
alpha = 0

s = "india got the independence in the year 1947"

for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        number += 1

print("Alphabets:", alpha)
print("Digits:", number)
print("Spaces:", space)