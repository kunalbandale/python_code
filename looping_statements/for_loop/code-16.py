"""
nested for loop
for var in iterable:
    for var in var: # will  act like a iterable
        # statement

* first outer lop will be executing
* then inner for loop will be executing
"""

a = [[1,2,3] , [4,5,6] , [7,8,9]]
for i in a:
    # print(i)
    for j in i:
        print(j)


"""
output:-
[1, 2, 3] --------> i
1 -> j
2 -> j
3 -> j
[4, 5, 6] --------> i
4 -> j
5 ->j
6
[7, 8, 9]
7
8
9
"""