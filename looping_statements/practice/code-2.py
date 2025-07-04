# reverse a list without using any built-in functions and slicing.
l = [1,2,3,4] # 4 ways try it
print(l[::-1])

print()
print()

for i in l[::-1]:
    print(i)

print()
print()

for i in reversed(l):
    print(i)



print()
print()

for i in range(-1,-len(l)-1  , -1):
    print(l[i] , end= " ")