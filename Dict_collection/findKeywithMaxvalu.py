d = {"a": 10, "b": 20, "c": 5}

max_key = max(d, key=d.get)
print(max_key)