# 4.wap to extract only individual data types form the list

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

for i in range(0,len(l)):
    if type(l[i]) in (str , bool , int , float):
        print((l[i]))