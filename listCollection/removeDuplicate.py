numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)

#####without set

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)