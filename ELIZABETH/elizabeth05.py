
def example():  ## example from the lecture
    x = 1
    while x < 3*5*7:
        if x%3==2 and x%5==3 and x%7==2:
            print("example = ",x)
            break
        x += 1
##example()


def prob_one(): ##Problem 1: x ≡ 3 (mod 11), x ≡ 4 (mod 13), x ≡ 5 (mod 17), x ≡ 6 (mod 19)
    x = 1
    while x < 11*13*17*19:
        if x%11==3 and x%13==4 and x%17==5 and x%19==6:
            print("problem 1 = ",x)
            break
        x += 1

##prob_one()

def prob_two():  ##Problem 2: 3x + 4y ≡ 5 (mod 13), 2x − 3y ≡ 4 (mod 11)
    print('Problem 2:')
    x = 1
    while x < 11*13:
        y = 1
        while y < 11*13:
            if (3*x+4*y)%13==3 and (2*x-3*y)%11==4:
                print(x,y)
                ##break
            y = y + 1
        x = x + 1
##prob_two()


def prob_3(): ##Problem 1: x ≡ 3 (mod 11), x ≡ 4 (mod 13), x ≡ 5 (mod 17), x ≡ 6 (mod 19)
    x = 1
    while x < 17*16*15:
        if x%17==3 and x%16==10 and x%15==0:
            print(x)
            
        x += 1

#prob_3()


##def Loan_Payoff_Schedule(): ##Problem 5: Loan Payment
loan = 10000
rate = .004
payment = 200
month = 0
interest = 0
principle = 0

while loan > 0 :
    month = month + 1
    interest = ( loan * rate)
    principle = payment - interest
    loan = loan - principle
    print(month, round(loan,2), rate, payment, round(interest,2), round(principle,2))

##Loan_Payoff_Schedule()  # pass in the parameters of Loan Amount, Interest Rate, Payment Amount

