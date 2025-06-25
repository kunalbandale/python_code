# 6.wap to find middle element is even or odd
# s=[3,4,6 ,7 ,9,1,5]

s = [3,4,6 ,2 ,9,1,5]

if len(s)%2 == 1:
    # print("odd length")
    res = (len(s) // 2)
    print("middle number" , s[res])
    if s[res] % 2 == 1:
         print("odd number")
    else:
        print("even number")
else:
    #print("even lenght")
    pass