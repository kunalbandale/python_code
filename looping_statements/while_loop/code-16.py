# .Write a program that appends the type of
# elements from a list.
# n = [23, 'Python',23.98]
#output:-->[<class 'int'>, <class 'str'>, <class 'float'>]

n = [23, 'Python',23.98]
i = 0
output = []
while i < len(n):
    output.append(type(n[i]))
    i += 1
print(output)



















