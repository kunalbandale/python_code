# list1 = ['program', 28, 9+4j, 'break', 24.2]
# vowel_dict = {}
#
# for i in list1:
#     if type(i) == str:
#         vowels = []
#         for j in i:
#             if j in 'AEIOUaeiou':
#                 vowels.append(j)
#         vowel_dict[i] = vowels
#
# print(vowel_dict)

d = {}
vow = ''
l = ['program', 28, 9+4j, 'break', 24.2]

for i in l:
    if type(i) == str:
        for j in i:
            if j in 'AEIOUaeiou':
                vow += j
        d[i] = vow
        vow = ''
print(d)
