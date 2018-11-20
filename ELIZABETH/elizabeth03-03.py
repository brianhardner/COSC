x = input('What is X?\n')
x = float(x)

numer = x**2 - 3 * x + 1
denom = x**2 - 5 * x + 6


if numer < 0:
    numer = -numer

if denom == 0:
     print(numer, denom, 'infinity')
else:
    q = numer / denom
    print(numer, denom, q)



