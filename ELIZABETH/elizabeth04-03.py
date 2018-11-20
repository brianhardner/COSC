def prob31():
    a=0
    for i in range(0,10001):
        ##print(a,i)
        a = a + i**2

    print(a)

##prob31()

def prob32():
    a=0
    for i in range(1,1001):
        ##print(a,i)
        a = a + 1 / (1+i**2)

    print(a)

##prob32()

def prob33():
    a=0
    for i in range(0,101):
        a = a + (-1)**i / (i+1)
        ##print(a,i)

    print(a,i)

##prob33()


def prob41():
    a=1
    for v in range(0,101):
        a = a * ((101-v) / (1+v))
        ##print(a,i)
    print(a,v)

##prob41()


def prob42(b,e):
    a=1
    for v in range(b,e):
        a = a * ((1+v) / (1+v**2))
        ##print(a,i)
    print(a,v)

prob42(0,101)
