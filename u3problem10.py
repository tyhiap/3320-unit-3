total_sum = 0
count = 0
num = int(input("Enter a number (or 0 to stop): "))

while num != 0:
    total_sum += num
    count += 1
    num = int(input("Enter a number (or 0 to stop): "))

if count > 0:
    average = total_sum / count
    print("Sum:", total_sum)
    print("Average:", average)
else:
    print("No numbers were entered.")
