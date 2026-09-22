total_sum = 0
num = int(input("Enter a number (or -1 to stop): "))

while num != -1:
    total_sum += num
    num = int(input("Enter a number (or -1 to stop): "))

print("The sum of the numbers is:", total_sum)
