data = [1, 2, 2, 3, 3, 3]

freq = {}
for i in data:
    freq[i] = freq.get(i, 0) + 1

print(freq)