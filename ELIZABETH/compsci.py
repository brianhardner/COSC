# # # # # # #
### LAB 7 ###
# # # # # # #

###############

def alice():
    with open('alice.txt','r') as f:
        for line in f:
            for word in line.split():
                if 'y' and 'z' and 'ing' in line and len(word) > 15:
                    print(line)
            #how do i get rid of those hyphens
                    
###############

def iris():
    with open('iris.csv', 'r') as f:
        for
#i get what its asking but how do i do

###############
            
def pop():
    with open('countries.txt', 'r') as f:
        for line

        #i have no freaking idea how to even start. again i know what its asking butttt

###############
def num():
    with open('numbers.txt', 'r') as f:
        for line in f:
            for digit in line.split():
                print("{0:10}".format(digit.replace(',',' ')))
                    #i dont know how to format this so the decimals are alligned

