# zip longest

"""
here also we can pass all the iterables
to overcome zip we have zip_longest()
"""
from itertools import zip_longest
a = "GOOD"
b = [1,2]
c = (1,2)
print(zip_longest(a,b,c)) # <itertools.zip_longest object at 0x0000017578F833D0>
for i in zip_longest(a,b,c):
    print(i)
print("^^^^^^^^^^^^^^^^^^^^^^^^")

print(list(zip_longest(a,b,c,fillvalue=0)))
# fill value in the place of null the fill value is be put


