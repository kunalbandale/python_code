# wap if a names ends with vowels then reverse a names else
# print its lenght

names = ["Kumar" , "Lakita" , "Umesh a" , "Priynaka" ,"elle"]
i = 0

while i < len(names):
    if names[i][::-1][0] in "aeiouAEIOU":
        print(names[i][::-1])
    else:
        print("LEN",len(names[i]))

    i = i + 1