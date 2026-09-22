first_input = None
last_input = None

for i in range(1, 6):
    num = float(input(f"Enter floating point number {i}: "))
    if i == 1:
        first_input = num
    if i == 5:
        last_input = num

average = (first_input + last_input) / 2
print("The average of the first and last input is:", average)
