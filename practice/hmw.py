import math

x = float(input('Enter a number: '))

if x <= -2:
    y = -3/x+1
elif -2 < x and x <= 0:
    y = math.fabs(x+1)
else:
    y = -x

print(y)