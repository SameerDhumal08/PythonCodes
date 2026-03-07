
for i in range(1,4):
    for j in range(1,4):
        print(i,",",j)

print('') #for new line

for i in range(1,6):
    for j in range(1,6):
        print("*",end=' ') #end='' for same line
    print('')

print('') #for new line

for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end=' ') #end='' for same line
    print('')

print('') #for new line

for i in range(1,6):
    print('*'*(6-i)) #end='' for same line
