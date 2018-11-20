
x=int(input("enter a number"))
numer=abs(x**2-3*x+1)
denom=x**2-5*x+6
if denom == 0:
    print("numer, denom, infinity")
else:
    q=numer/denom
    print(q)
    