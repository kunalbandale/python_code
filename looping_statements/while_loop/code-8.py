# wap to print the name which is starting with vowel in the givn list

names = ["agra" , "bangalore" , "mumbai" , "pune" , "indore" , "isha" , "surat" , "eshwar"]
i = 0

while i < len(names):
    # print(names[i])
    if names[i][0] in "aeiouAEIOU":
       print(names[i])
    i = i + 1