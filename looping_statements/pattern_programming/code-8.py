"""
print digonal
primary digonal
$ # # #
# $ # #
# # $ #
# # # $

secondary digonal
# # # %
# # % #
# % # #
% # # #

"""
row = int(input("Enter no of rows"))
col = int(input("Enter no of cols"))

for i in range(1,row+1):
    for j in range(1,col+1):
        if i == j:
            print("#" , end=" ")
        else:
            print(' ' , end=" ")
    print()