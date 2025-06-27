# wap to print only vowels and numbers

s = "hello123"

i = 0
print(len(s))

while i < len(s):
    if s[i] in 'aeiouAEIOU' or s[i].isdigit():
        print(s[i])
    i = i + 1
    