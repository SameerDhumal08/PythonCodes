numbers = [10, 20, 4, 45, 99]

numbers.sort()
second_largest = numbers[-2]

print("Second Largest:", second_largest)

#without inbuilt fun

numbers = [10, 20, 4, 45, 99]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)
