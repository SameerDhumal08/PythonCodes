
import math
a = int(input('Write a value of a:'))
b = int(input('Write a value of b:'))
c = int(input('Write a value of c:'))

r1 = (-b + math.sqrt(b **2 - 4*a*c))/(2*a)
r2 = (-b - math.sqrt(b **2 - 4*a*c))/(2*a)

print('Roots of equation are: ',r1,r2)