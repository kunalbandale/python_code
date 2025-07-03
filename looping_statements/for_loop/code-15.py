"""
# output {h: ["hi" , "hello"] , g: ["good"]}
s = "hi hello good morning welcome to python session"

# Split the string into words
words = s.split()

# Initialize the output dictionary
output = {}

# Define the target starting letters
target_letters = ['h', 'g' , 'm' , 'w' , 't' , 'p' , 's']


# Iterate through each word
for word in words:
    first_letter = word[0]
    if first_letter in target_letters:
        output.setdefault(first_letter, []).append(word)

print(output)
"""
