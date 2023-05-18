# getting number1,number2 for start and end of range
num1 = int(input("enter your first number for start of range : "))
num2 = int(input("enter your two number for end of range: "))
# The formula for calculating the prime number
for number in range(num1, num2 + 1):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                break
        else:
            print(number)
