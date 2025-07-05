l = [1,2,3,4,5,6,7,10]
k = []
for i in range(1,11):
    if i not in l:
        k.append(i)
print(k)
#
l = [1, 2, 3, 4, 5, 6, 7, 10]
n = 10

expected_sum = n * (n + 1) // 2
actual_sum = sum(l)
missing_sum = expected_sum - actual_sum

print("Sum of missing numbers:", missing_sum)
