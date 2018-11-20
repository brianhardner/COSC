x = input('What is X?: ')
x = float(x)

if x < 0:
    print('Value can not be negative')
elif x < 0.5:
    print('minimal')
elif x < 3.0:
    print('small')
elif x < 7:
    print('medium')
elif x < 9.5:
    print("large")
elif x <= 10: 
    print('i cant read this in the image')
else:
    print('Value can not be greater than 10')
