t = {1:2,2:3,3:4}

for i in t:
    print(t[i])  # varName[key]

print('------------------')

for i in t.items():
    print(i)


print('------------------')

k = "good day"
# wap I want output in dict format {g:asciivalue}
# var[key] = value
# var.update({key:value})

d = {}

for i in k:
    d[i] = ord(i)
print(d)
#
# for i in k:
#     d.update(i:ord(i))
# print(d)

t = [1,True,"abc",3+4j,89.90,[1,2,3],{4,5,6}]

# while loop

i=0

while i < len(t):
    if isinstance(t[i],(int,float,complex,bool)):
        print(t[i])
    i = i + 1

print()
print()

for j in t:
    if isinstance(j,(int , float , complex , bool)):
        print(i)

print()
print()