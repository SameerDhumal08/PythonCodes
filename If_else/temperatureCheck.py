#Temperature check

temp = int(input("Enter temperature: "))

if temp > 30:
    print("Hot")
elif temp >= 20:
    print("Normal")
else:
    print("Cold")