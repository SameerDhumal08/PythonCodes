
s = 'Hello How are you'
x = s.find('H',1,len(s))
print(x)

s = 'Hello How are you'
x = s.find('a')
print(x)

s = 'Hello How are you'
x = s.find('o',5)
print(x)

s = 'Hello How are you'
x = s.find('o',5,7)
print(x)  #shows that string is not found in between 5 to 7 so gives -1

s = 'Hello How are you'
x = s.find('How')
print(x)  #shows that string is not found in between 5 to 7 so gives -1

#Reverse find
s = 'Hello How are you'
x = s.rfind('o')
print(x)

#Index
s = 'Hello How are you'
x = s.index('o')
print('index of alphabet: ',x)

s = 'Hello How are you'
x = s.index('o') #if index alphabet not found it will gives an exception
print('index of alphabet: ',x)

s = 'Hello How are you'
x = s.count('o')
print('Count of alphabet: ',x)




