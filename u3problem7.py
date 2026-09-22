num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    current = num1
    target = num2
else:
    current = num2
    target = num1

while current >= target:
    print(current)
    current -= 1
