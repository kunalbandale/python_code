# wap to check which is the smallest value among 3 number

a = eval(input("Enter Any Number1"))
b = eval(input("Enter Any Number2"))
c = eval(input("Enter Any Number3"))

# for smallest
if a < b and a < c:
    print(f"{a} is smallest")
elif b < a and b < c:
    print(f"{b} is smallest")
else:
    print(f"{c} is smallest")

#  for greatest
if a > b and a > c:
    print(f"{a} is greater")
elif b > a and b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")


# using built-in min() function
print(min(a,min(b,c)))
print(max(a,max(b,c)))
