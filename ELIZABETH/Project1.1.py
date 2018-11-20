import string
import collections

global_offset = ord('A')
global_length = ord('Z')-ord('A')+1

def clean(infilename, outfilename):
    """
    Takes a textfile and creates a new copy without punctuations and
    newlines.  All letters are translated to capital letters. The
    translation will loose digits as well. 
    """
    with open(infilename, encoding="latin-1") as infile, open(outfilename, "w", encoding="utf8") as outfile:
        for line in infile:
            newline = []
            for letter in line.strip():
                if line.startswith("Illustration:"):
                    continue
                if letter in string.ascii_letters:
                    newline.append(letter.upper())
            print("".join(newline), file = outfile, end="")
    print("done")
    return

def cipher(infilename, outfilename, password):
    """
    A function that encrypts infilename with the Vigenere cipher
    using secret key password and writes the result to outfilename.
    Outfilename contains a single long line.
    """
    count = 0
    print(len(password))
    with open(infilename, encoding="latin-1") as infile, open(outfilename, "w", encoding="utf8") as outfile:
        buffer = infile.read()
        outputbuffer = []
        for letter in buffer:
            index = count%len(password)
            newletter = change(letter, password[index])
            outputbuffer.append(newletter)
            count+=1
        print("".join(outputbuffer), file=outfile)
    return count

def decipher(infilename, outfilename, password):
    """
    Assumes that infilename has been encrypted with the Vigenere cipher
    that 
    """
    count = 0
    with open(infilename, encoding="latin-1") as infile, open(outfilename, "w", encoding="utf8") as outfile:
        buffer = infile.read()
        outputbuffer = []
        for letter in buffer:
            index = count%len(password)
            newletter = unchange(letter, password[index])
            outputbuffer.append(newletter)
            count+=1
        print("".join(outputbuffer), file=outfile)
    return count


def change(letter, pwd):
    """
    changes a capital letter by adding the capital letter pwd in the
    Caesar cipher
    """
    return chr( (ord(letter)+ord(pwd)-2*global_offset)%global_length+global_offset)

def unchange(letter, pwd):
    """
    undoes the change from the function change
    """
    return chr( (ord(letter)-ord(pwd)+global_length)%global_length + global_offset)
    
def caesar(string, pwd):
    """
    Encrypts the string using Caesar's cipher with letter pwd and
    returns the encrypted string.
    """
    result = []
    for letter in string:
        result.append(change(letter, pwd))
    return "".join(result)
            
     
                
# ------------------------------------------------------------------------------------ 
# # for my development work i used the alice.txt file from previous excercises
# i first cleaned then encryped it using the routines provided
# this way i could peak inside the files to see how each letter was encryped
# ------------------------------------------------------------------------------------ 
#clean("alice.txt","alice_clean.txt")
#cipher('alice_clean.txt', 'alice_encrypt.txt','LOYOLACHICAGO')
#decipher('alice_encrypt.txt', 'alice_decrypt.txt','LOYOLACHICAGO')


# ------------------------------------------------------------------------------------ 
# def displacement(infilename):
# this routine compares every letter in the encoded document to other leters
# a certain distance or displacement away from each letter.
# in the first pass we compare letter 1 to letter 2, letter 2 to letter 3 and increment
# a counter when they match.  In the second pass we compare letter 1 to letter 3
# letter 2 to letter 4 and count when they match and so on through the number of
# itterations which i set to 100 (e.g. compare letter 1 to letter 100, letter 2 to 
# letter 101...). In the end, we then look to find the first displacement (displace)
# that sticks out as compared to the others (e.g. > 25% higher).  This displacement 
# is the length of the password and is the first encoded 'E'. 
# ------------------------------------------------------------------------------------ 
def displacement(infilename):
    displace = 1
    itterations = 100
    results = dict()
    highest_count = 0
    offset = 0

    with open(infilename, encoding="latin-1") as infile:
        buffer = infile.read()
 
        while displace <= itterations:
            count = 0
            match_counter = 0
         
            while count < len(buffer)-displace:                 # need to subract 'displace' from the length
                if buffer[count] == buffer[count+displace]:     # so you don't go past the end of the buffer
                    match_counter = match_counter + 1
                    #print(buffer[count], buffer[count+displace])
                count = count + 1
            results[displace] = match_counter

            #print(displace) #This will show you which displacement itteration you are on
            #this next IF statement will find the first displace value that "sticks out" 
            if results[displace] >1.25*highest_count:
                highest_count = results[displace]
                offset = displace
            
            displace = displace + 1
        
        print(results)
        print('The password length is:',offset)        
        return offset

password_length = displacement('cipher.txt')
#password_length = 15

def find(infilename, displacement):
    password = ''                                 # as we find letters we will assemble them here
    with open(infilename, encoding="latin-1") as infile:
        buffer = infile.read()
        
        for password_position in range(0,displacement):    # for each position in the password (e.g. 1 through 15)
            d = dict()
            for buffer_position in range(password_position,len(buffer),displacement):
                if buffer[buffer_position] not in d:
                    d[buffer[buffer_position]] = 1
                else:
                    d[buffer[buffer_position]] += 1
            #print (d)       
            #print (max(d.values()))

            highest = 0
            for index in d:             # find the encrypted letter with the most
                if d[index] > highest:  # occurances.  this is your next encrypted E
                    highest = d[index]
                    letter = index
            
            x = 65-69+ord(letter)       # rember, (letter) is the encryped letter. Need to convert it.
            if x < 65:                  # 69 is ord(E), 65 is ord(A).  if x is too low you need to add 26 to 
                x=x+26                  # wrap around the alpabet
            password += chr(x)
            print ('Password letter is: ', chr(x))
    print('The password is: ',password)


find('cipher.txt', password_length)

decipher('cipher.txt', 'decipher.txt','JOLIETMARQUETTE')
