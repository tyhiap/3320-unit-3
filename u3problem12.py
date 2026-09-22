third_input = None

for i in range(1, 6):
    num = int(input(f"Enter integer {i}: "))
    if i == 3:
        third_input = num

print("The third input was:", third_input)
