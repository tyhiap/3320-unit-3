total = 0
x = 1

while x <= 5:
    num = float(input(f"Enter number {x}: "))
    total += num
    x += 1

average = total / 5
print("The average of the numbers is:", average)
