a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a) & set(b)
print(common)

#without set
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for i in a:
    if i in b:
        common.append(i)

print(common)

#Without set() and without in

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for i in a:
    for j in b:
        if i == j:
            common.append(i)

print(common)
