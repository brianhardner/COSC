import string
import collections

global_offset = ord('A')
global_length = ord('Z')-ord('A')+1
password_length = 0
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
    

def find(infilename, displacement):
    pass

def caesar(string, pwd):
    """
    Encrypts the string using Caesar's cipher with letter pwd and
    returns the encrypted string.
    """
    result = []
    for letter in string:
        result.append(change(letter, pwd))
    return "".join(result)
            
     
                
#clean("alice.txt","alice_clean.txt")
#cipher('alice_clean.txt', 'alice_encrypt.txt','BRIOLACHICAGO')
#decipher('alice_encrypt.txt', 'alice_decrypt.txt','LOYOLACHICAGO')


def displacement(infilename):
    displace = 1
    itterations = 4*26
    results = dict()
    best_disp = 0
    offset = 0

    with open(infilename, encoding="latin-1") as infile:
        buffer = infile.read()
        while displace <= itterations:
            count = 0
            match_counter = 0
            while count < len(buffer)-displace:
                if buffer[count] == buffer[count+displace]:
                    match_counter = match_counter + 1
                    #print(buffer[count], buffer[count+displace])
                count = count + 1
            results[displace] = match_counter

            #print(displace)
            if results[displace] >1.25*best_disp:
                best_disp = results[displace]
                offset = displace
            
            displace = displace + 1

        #print(offset, best_disp)
        #print(buffer[13],' = E')
        
        d = dict()
        for i in range(0,len(buffer),13):
            if buffer[i] not in d:
                d[buffer[i]] = 1
            else:
                d[buffer[i]] += 1
        print (d)       
        print (max(d.values()))

        highest = 0
        for i in d:
            if d[i] > highest:
                highest = d[i]
                letter = i
        
        print (letter, ord(letter)    ,'first letter is: ', chr(65-69+ord(letter))        )
    
        d = dict()
        for i in range(1,len(buffer),13):
            if buffer[i] not in d:
                d[buffer[i]] = 1
            else:
                d[buffer[i]] += 1
        print (d)       
        print (max(d.values()))        

        highest = 0
        for i in d:
            if d[i] > highest:
                highest = d[i]
                letter = i
                
        print (letter, ord(letter)    ,'second letter is: ', chr(65-69+ord(letter))        )

        d = dict()
        for i in range(2,len(buffer),13):
            if buffer[i] not in d:
                d[buffer[i]] = 1
            else:
                d[buffer[i]] += 1
        print (d)       
        print (max(d.values()))        

        highest = 0
        for i in d:
            if d[i] > highest:
                highest = d[i]
                letter = i
        
        x = 65-69+ord(letter)
        if x < 65:
            x=x+26

        print (letter, ord(letter)    ,'third letter is: ', chr(x)        )


displacement('alice_encrypt.txt')