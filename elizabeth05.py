def example():
    x = 1
    while x < 3*5*7:
        if x%3==2 and x%5==3 and x%7==2:
            print(x)
            ##break
        x=x+1

##example()

def problem_one():
    x = 1
    while x < 11*13*17*19: 
        if x%11==3 and x%13==4 and x%17==5 and x%19==6:
            print(x)
            ##break
        x=x+1

##problem_one()

def problem_two():
    x = 1
    while x < 11*13:
        y = 1
        while y < 11*13:
            if (3*x+4*y)%13==5 and (2*x-3*y)%11==4:
                print(x,y)
                ##break
            y=y+1
            
        x=x+1
    print("end")

problem_two()


