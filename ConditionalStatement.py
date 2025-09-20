a = 2
b = 6
c = 3

print(a<c)
print(a>b)

print(a<b and b>c)

#Conditional statement for eligibility
age = int(input('Enter a age:'))

if age >= 18:
    print('Eligible for vote')
else :
    print('Not eligible for vote')

#Nested if and elif
amount =  int(input('Enter amount:'))
total =0
if amount < 1000:
    total = amount - amount * 0.1

elif amount >= 1000 and amount < 5000:
    total = amount - amount * 0.15

elif amount >= 5000 and amount < 10000:
    total = amount - amount * 0.2

print('total is :',total)

