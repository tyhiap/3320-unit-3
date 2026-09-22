rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol: ")

print("\n--- Version 1 Example ---")
for i in range(1, rows + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()

print("\n--- Version 2 Example ---")
for i in range(rows, 0, -1):
    for j in range(i):
        print(symbol, end=" ")
    print()
