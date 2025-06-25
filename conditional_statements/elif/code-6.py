# wap to give discount to customer based on total price p1+p2+p3
# 1000-3000 500 discount and 3001 to 5000 price 1000
# discount more than 5001 price
# 1200 discount and less than 1000 price no discount

p1 = eval(input("Enter the amount "))
p2 = eval(input("Enter the amount "))
p3 = eval(input("Enter the amount "))

totalAmount = (p1+p2+p3)
print(totalAmount)

if totalAmount <= 1000:
    print("no discount")
elif totalAmount >= 1000 and totalAmount<=3000:
    print(f"total amount is {totalAmount} and after discount | final amount is {totalAmount-500}")
else :
    pass # todo