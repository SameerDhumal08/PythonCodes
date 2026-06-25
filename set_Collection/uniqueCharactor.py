text = "hello world"
unique_chars = set(text)

print(len(unique_chars))

##without set
text = "hello world"

unique_chars = []

for char in text:
    if char not in unique_chars:
        unique_chars.append(char)

print(len(unique_chars))
