nums = [1, 2, 4, 6]
n = 6

missing = set(range(1, n+1)) - set(nums)
print(missing)