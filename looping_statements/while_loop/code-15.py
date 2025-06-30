# Write a Program to separate positive and negative number
# from a list.
# a=[1,2,3,4,-90,-45,-33,-87]
#output
# Positive=[1,2,3,4]
# Negative=[-90,-45,-33,-87]




a = [1,2,3,4,5,6,-90,-45,-74,25,-44,-853]
positive = []
negative = []
i = 0

while i < len(a):
    if a[i] > 0:
        positive.append(a[i])
    else:
        negative.append(a[i])
    i = i + 1

print(positive)
print(negative)











