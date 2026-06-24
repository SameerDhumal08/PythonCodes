numbers = [1, 2, 3, 4, 5]

numbers.reverse()
print(numbers)

#with new list

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)

#without new list

numbers = [1, 2, 3, 4, 5]

start = 0
end = len(numbers) - 1

while start < end:
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start += 1
    end -= 1

print(numbers)
