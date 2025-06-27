# wap to print the names only if the lenght of the names is even

l = ["ramrakj" , "pailkk" , "kunal", "bandae" , "prakash" , "shakar" , "dev"]
i = 0

while i < len(l):
    if len(l[i]) % 2 == 0:
        print(l[i])
    i = i + 1
