#prefix confirm the string starts with
s = "python is very easy"
s1 = s.startswith('python')
print(s1)
s2 = s.endswith('easy')
print(s2)

#remove prefix
s3 = s.removeprefix('py')
print(s3)
#remove suffix
s4 = s.removesuffix('sy')
print(s4)

#partioning string
s5 = s.partition("th")
print(s5)

s6 = s.rpartition('y')#reverse partioning
print(s6)