# wap to check a data is a sequence/iterable.individual data type
# set | dict -> iterable not seq
# int float str boolean complex - > individual data type
# string list tuple -> sequence

# ====================================================
# using isinstance() function
# ====================================================


data = eval(input("Enter Any Data / Element :"))

if isinstance(data,(str,list,tuple)):
    print("Sequence Data Type")
elif isinstance(data,(set,dict)):
    print("Iterable Data Type")
elif isinstance(data,(int,float,complex,bool)):
    print("Individual Data Type")
else:
    print("Enter Valid Data")

# ====================================================
# using type() function
# ====================================================

if type(data) in (str,list,tuple):
    print("Sequence Data Type")
elif type(data) in (set,dict):
    print("Iterable Data Type")
elif type(data) in (float , int , complex , bool):
    print("Individual Data Type")
else:
    print("Enter Valid Data")



