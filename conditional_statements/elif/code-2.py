# wap if input is string return its length , else if input is list pop element ,
# else if input is tuple reverse else invalid input

data = eval(input("Enter Any Data / Element"))

if isinstance(data,str):
    print(len(data))
elif isinstance(data,list):
    print("popped element" , data.pop())
elif isinstance(data,tuple):
    print(data[::-1])
else:
    print("Enter a Valid Data")
