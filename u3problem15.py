current_year = int(input("What is the current year? "))

print("Year\tIncrease in mm")
print("----------------------")

# Evaluates the current year to 25 years ahead, in increments of 5
start_year = current_year
for year in range(start_year, start_year + 26, 5):
    years_passed = year - start_year
    increase = years_passed * 1.7
    print(f"{year}\t{increase:.1f}")
