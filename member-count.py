# getting Letters from user
letters = input("enter your Letters : ")
# Creating a dictionary to store the number of letters
letters_count = {}
# Program logic
for char in letters:
    if char not in letters_count:
        count = letters.count(char)
        letters_count[char] = count
print(letters_count)
