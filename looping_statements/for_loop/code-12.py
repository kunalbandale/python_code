# wap to create a dict index and word pair

# d = {1:"learn" , 2: "study" , 3:"python" , 4:"java"}
s = "tomorrow is weekend and non-veg special"
# print(s.split())
d = {}

for i,j in enumerate(s.split()):
    d[i] = j
print(d)
