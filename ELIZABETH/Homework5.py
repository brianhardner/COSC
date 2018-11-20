
############################################
## Convert a letter to a number
############################################
def letter2number(letter):
    if letter in "ABCabc":
        return 2
    elif letter in "DEFdef":
        return 3
    elif letter in "GHIghi":
        return 4
    elif letter in "JKLjkl":
        return 5
    elif letter in "MNOmno":
        return 6
    elif letter in "PQRSpqrs":
        return 7
    elif letter in "TUVtuv":
        return 8
    elif letter in "WXYZwxyz":
        return 9

a = letter2number('I')
print('Convert a letter to a number: ',a)

############################################
##  Convert a Sting of Letters to a Number
############################################
def name2number(name):
    xnum='' 
    for letter in name:
        xnum = xnum + str(letter2number(letter))
    return xnum

b = name2number('DAVID')
print('Convert a Sting of Letters to a Number: ',b)


############################################
##  Remove 0's and 1's from a number
############################################

def no_zeros_or_ones(anum):
    bnum=''
    for digit in anum:
        if digit in "23456789":
            bnum = bnum + digit
    
    return bnum

c = no_zeros_or_ones('3284310')
print('Remove 0s and 1s from a number: ',c)



############################################
##  Look up a name in the first.txt file.
##  This was just for practice and isn't 
##  used elsewhere
############################################
def lookup_name(name):
    name_dict = dict()
    fin = open('first.txt')
    for line in fin:
        row = line.strip()
        words = row.split()
        if words[0] == name:
            n=''
            for c in words[0]:
                n = n + str(letter2number(c))
            name_dict[words[0]] = n
            print('Look up a name in the first.txt file.',words[0],name_dict[words[0]])

lookup_name('DAVID')

############################################
##  Create a phone list of numbers and names
##  using a dictionary.
############################################
def create_phonelist():
    num_dict = dict()
    fin = open('first.txt')
    for line in fin:
        row = line.strip()
        words = row.split()
        n=''
        for c in words[0]:
            n = n + str(letter2number(c))
        num_dict[n] = words[0]
    return num_dict

phonelist = create_phonelist()
print('Lookup using a dictionary: ',phonelist['32843'])
print('Lookup using a dictionary: ',phonelist['27426'])

############################################
##  Create a phone list of numbers and names
##  using a two lists.
############################################
def create_lists():
    fin = open('first.txt')
    for line in fin:
        row = line.strip()
        words = row.split()
        n=''
        for c in words[0]:
            n = n + str(letter2number(c))
        name_list.append(words[0])
        num_list.append(n)

global name_list, num_list
name_list = []
num_list = []
create_lists()

for k in range(len(num_list)):
    if num_list[k] == '32843':
        print('Lookup using lists: ', name_list[k])





## IGNORE BELOW
##def create_phonelist():
##    ##name_dict = dict()
##    num_dict = dict()
##    fin = open('first.txt')
##    for line in fin:
##        row = line.strip()
##        words = row.split()
##        n=''
##        for c in words[0]:
##            n = n + str(letter2number(c))
##        ##name_dict[words[0]] = n
##        num_dict[n] = words[0]
##        ##print(words[0],name_dict[words[0]])
##    return num_dict

##reverse lookup
##for k in phonelist:
##    if phonelist[k] == '53484':    ##32843
##        print(k,phonelist[k])
##print(phonelist['DAVID'])


