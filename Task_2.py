# 2. The Greatest Showdown
# Task 2: Identify the Smallest
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
print(f"The smallest number among {num1}, {num2}, and {num3} is: {smallest}")