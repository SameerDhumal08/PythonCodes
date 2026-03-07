

s1 = "Hello World"
print(s1[1:5])
print(s1[:5])
print(s1[:])
print(s1[::2])
print(s1[::-1]) #backword direction
print(s1[:5:])
print(s1[-3::-1])
print()


####Reverse string
text = "Hello World"
words = text.split()   # splits into ['Hello', 'World']
reversed_text = " ".join(words[::-1])   # joins as 'World Hello'
print(reversed_text)