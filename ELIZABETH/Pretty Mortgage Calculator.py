

def mortgage():
    print('****************************************')
    print('**  The Ultimate Mortgage Calculator  **')
    print('****************************************')
    princ = float(input('What is the prinipal '))
    rate = float(input('"What is the interest rate (in percents) '))/1200
    print('Your minimum rate is ', round(rate*princ,2))
    paym = float(input('What is the monthly payment '))
    print('This is what your mortgage scheme looks like')
    print('Month    Interest      Principle     Payment')
    month = 0
    while princ > 0:
        intpaid = princ*rate
        princ = princ + princ*rate - paym
        month += 1
        #print(month, intpaid, princ, paym)

        #print("{0}".format(month))
       
        if princ < 0:
            lastpayment = paym + princ
            princ = 0
            print("{0:>3}     {1:>8.2f}       {2:>8.2f}     {3:>8.2f}".format(month, intpaid, princ, lastpayment))
        else:
            print("{0:>3}     {1:>8.2f}       {2:>8.2f}     {3:>8.2f}".format(month, intpaid, princ, paym))


mortgage()

