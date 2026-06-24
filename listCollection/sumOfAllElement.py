numbers = [10, 20, 30, 40]

total = sum(numbers)
print("Sum:", total)

#without inbuilt 
numbers = [10, 20, 30, 40]

total = 0

for i in numbers:
    total = total + i

print("Sum:", total)

###
numbers = [10, 20, 30, 40]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

print("Sum:", total)
