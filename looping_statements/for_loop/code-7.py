# 2.wap to extract vowels and digits in a string
# s="hello123"

s = "hello123"
vowels = "aeiouAEIOU"
extracted_vowels = []
extracted_digits = []

for char in s:
    if char in vowels:
        extracted_vowels.append(char)
    elif char.isdigit():
        extracted_digits.append(char)

print("Vowels:", extracted_vowels)
print("Digits:", extracted_digits)



