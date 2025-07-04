"""
wap to create a dict word and reerse word pair
s = "tomorrow is weekend and non-veg special
o/p {tomorrow:'worromot' , 'is' : 'is' , 'weekend' .... }
"""

s = "tomorrow is weekend and non-veg special"
d = {}
# print(s.split())

for i in s.split():
    d[i]=i[::-1]
print(d)