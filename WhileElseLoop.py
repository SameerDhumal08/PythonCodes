###########################
count = 1
while count <= 10:
    print(count)
    count += 1
else:
    print('printed all 10 numbers')
print('end of program')

###########################
count = 1
while count <= 10:
    print(count)
    count += 1
    if count>5:
        break # this statement will stop loop and else condition
else:
    print('printed all 10 numbers')
print('end of program')