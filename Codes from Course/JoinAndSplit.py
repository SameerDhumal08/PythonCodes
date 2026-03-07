
#replace with - with commas
s= "a-b-c-d-e"
x = s.replace("-",",")
print(x)

#replace with - with commas only starting 3
s= "a-b-c-d-e"
x = s.replace("-",",",3)
print(x)

#replace no present it will print as it is
s= "a-b-c-d-e"
x = s.replace("k","m")
print(x)

#replace no present it will print as it is
s= "sameer@gmail.com"
x = s.replace("gmail","yahoo")
print(x)

#Join
s1 = "abc"
s2 = "xyz"
x = s1.join(s2)
print(x)

s1 = "/"
s2 = "xyz"
x = s1.join(s2)
print(x)

#Split
s1 = "Hello World python"
x = s1.split()
print(x)

s1 = "Hello-World-python-script-AI-ML"
x = s1.split("-",3)
print(x)