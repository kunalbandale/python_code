row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

if row != col:
    print("For this pattern, rows and columns must be equal.")
else:
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if i + j == 6:
                print('$', end=" ")
            else:
                print('#', end=" 88")
        print()