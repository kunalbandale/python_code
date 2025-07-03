x = "programming"

# for i in range(len(x)):
#     print(i,x[i])

# without using range function if we want to do the same task

"""
enumerate() -> inbuilt class 

syntax:- 
enumerate(iterable)
print(enumerate(iterable)) -> obj address 

syntax 2 :- looping syntax

for variable in enumerate(iterable):
        # statement 
"""
print(enumerate(x)) # <enumerate object at 0x000001AB59A3F580>
print(list(enumerate(x)))
# output
# [(0, 'p'), (1, 'r'), (2, 'o'), (3, 'g'), (4, 'r'), (5, 'a'), (6, 'm'), (7, 'm'), (8, 'i'), (9, 'n'), (10, 'g')]
# (0, 'p')


for i in enumerate(x):
    print(i) # (0, 'p')
