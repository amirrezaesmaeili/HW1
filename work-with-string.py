# A list of vowels
Vowels = ["a", "e", "i", "u", "A", "E", "I", "O", "U", "o"]

# Getting the name from the user
name = input("enter your name : ").split(" ")
nameNoneSpace = "".join(name)

# Convert vowels to dots
for char in nameNoneSpace:
    if char in Vowels:
        nameNoneSpace = nameNoneSpace.replace(char, ".")

# Reverse nameNone space characters
print(nameNoneSpace.swapcase())
