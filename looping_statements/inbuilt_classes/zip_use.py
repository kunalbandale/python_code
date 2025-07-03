# zip()

# why to use
"""
one of the inbuilt class
* if we want to match pos to pos
* in zip inbuilt class we can use all iterable (str,list,tuple,set,dict)
* in zip while passing iterable length should be equal
* if length not match data loss will happen
a = [1,  2,  3,  4]
b = [11, 12, 13, 14]

syntax:-
zip(v1,v2,v3,...........,)
print(zip(v-v1,..,))-> obj address
"""

a = [1,2,3,4,5]
b = [4,5,6,7,8]

print(zip(a,b)) # <zip object at 0x000001CFC0A3F600>
print(list(zip(a,b))) # [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
print(set(zip(a,b)))
print(tuple(zip(a,b)))
print(dict(zip(a,b)))
print('-----------------')

for i in zip(a,b):
    print(i)

print('$$$$$$$$$$$$$$$$$$$$$$')
a = "GOOD"
b = [1,2]
c = (1,)

print(list(zip(a,b,c)))
print("$$$$$$$$$$$$$$$$$$$$$$")
for i in zip(a,b,c):
    print(i)