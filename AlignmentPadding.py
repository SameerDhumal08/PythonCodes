#Alignment and Padding in string
s = "Hello"
x = s.ljust(7,"*")
print(x)

s = "Hello"
x = s.rjust(7,"*")
print(x)

s = "Hello"
x = s.center(7,"*")
print(x)

s = "Hello"
x = s.zfill(7)
print(x)

###Strip Method (remove spaces and charactor in string)

s = "  Hello  "
x = s.rstrip()
print(x)

s = "___Hello___"
x = s.rstrip("_")
print(x)
x = s.lstrip("_")
print(x)
x = s.strip("_")
print(x)

s = "#!Hello  $ *"
x = s.strip("#! $*")# remove multiple symbols
print(x)