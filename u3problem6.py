countdown = int(input("Enter a number to countdown from: "))

while countdown >= 0:
    if countdown == 5:
        print(f"{countdown} Almost there!")
    elif countdown == 0:
        print(f"{countdown} Happy Lunar New Year!")
    else:
        print(countdown)
    countdown -= 1
