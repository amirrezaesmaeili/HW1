# Method one :
number = int(input("enter your number : "))
reverseNumber = 0
while number > 0:
    remain = number % 10
    reverseNumber = (reverseNumber * 10) + remain
    number = number//10
print(reverseNumber)

# method two :

number2 = int(input("enter your number2 for other method : "))
print(str(number2)[::-1])
