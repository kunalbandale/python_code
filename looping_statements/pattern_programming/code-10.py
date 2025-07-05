row = 6
col = 6

for i in range(1,row+1):
    for j in range(1,col+1):
        if i+j == 6 and i ==j:
            print('*', end=" ")
        else:
            print('&' , end=" ")
    print()