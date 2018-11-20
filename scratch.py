import math
def mysqrt(a):
    x = a - .99
    while True:
        ##print(x)
        y = (x + a/x) / 2
        if y == x:
            print(a, y, math.sqrt(a), y-math.sqrt(a))
            break
        x=y

a=1
while a <= 10:
  mysqrt(a)
  a=a+1

