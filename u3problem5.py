print("--- Method 1: Counting down by 2 starting from an odd number ---")
x = 19
while x >= 1:
    print(x)
    x -= 2

print("\n--- Method 2: Counting down by 1 with a conditional modulo check ---")
x = 20
while x >= 1:
    if x % 2 != 0:
        print(x)
    x -= 1

print("\n--- Method 3: Using a while True loop with a break statement ---")
x = 20
while True:
    if x < 1:
        break
    if x % 2 != 0:
        print(x)
    x -= 1
