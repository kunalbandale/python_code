# wap to print even positional charcters in the given string
s = "hello world"
# output = > h l o w r d

i = 0 # pointing to pos
while i < len(s):
    print(s[i] , end = " ")
    i = i + 2