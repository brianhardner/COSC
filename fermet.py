def fermat():
    N = powN;
    while N >=3:
        N = int(input("Please enter pow > 2: \n"));
    if (a**N) + (b**N) == (c**N):
        print("Fermat is wrong my holy!!");
    else:
        print("That doesn't work");

a = int(input("Enter x: \n"));
b = int(input("Enter y: \n"));
c = int(input("Enter z: \n"));
powN = int(input("Enter pow: \n"));

fermat();