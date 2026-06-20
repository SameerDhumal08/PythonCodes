numbers = [1, 2, 3, 2, 4, 2, 5]

count = numbers.count(2)
print("Count:", count)

##### count the target number without using inbuit fun

numbers = [1, 2, 3, 2, 4, 2, 5, 3]
target = 2

count = 0

for num in numbers:
    if target == num:
        count=count + 1

print("Count : ",count)