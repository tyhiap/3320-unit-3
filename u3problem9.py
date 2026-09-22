sentinel = int(input("Enter a number that will end the loop (sentinel value): "))

total_sum = 0
count = 0

while True:
    num = int(input(f"Enter a number (or {sentinel} to stop): "))
    if num == sentinel:
        break
    total_sum += num
    count += 1

if count > 0:
    average = total_sum / count
    print("Sum:", total_sum)
    print("Average:", average)
else:
    print("No valid numbers were entered.")
