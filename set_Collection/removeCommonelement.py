a = {1, 2, 3}
b = {3, 4, 5}

common = a & b
a -= common
b -= common

print(a, b)