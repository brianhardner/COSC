###########################################################################
#  Simple prompt.  Only checks to see if the input is a positive integer
#  A better prompt would allow for decimals and negative numbers
###########################################################################

def get_number():
    x = ''
    Message = 'Please enter an integer number: '
    while not(x.isnumeric()):     #The method ".isnumeric" returns TRUE if all chars in 'x' are numbers
        x = input(Message);
        Message = 'That wasnt an integer number. Please try again: '
    return x
    
#get_number()



###########################################################################
#  Scan Through a File and count a bunch of stuff
#  ------------------------------------------------------------------------
#  The key here is to develop in steps.  Dont try to code it all at once.
#  Write in small blocks and test along the way by printing messages to 
#  yourself.  I wrote this is three BIG Steps.  Step one was to answer
#  part 2a of the assignment.  I started by taking the code from from 
#  Homework 5  on reading fiels and addapted it to count rows and words,
#  then eventually letters.  After that worked, I layered in part 2b and 2c
#  which looked to could up words and lines with special characters and
#  lengths. 
###########################################################################
def scan_a_file():
    fin = open('alice.txt')
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    yY = 'yY'
    zZ = 'zZ'
    aA = 'aA'
    num_lines   = 0
    num_words   = 0
    num_letters = 0
    long_words  = []
    lines_no_As = []

    for line in fin:
        line = line.strip()
        num_lines = num_lines + 1
        
        num_aA = 0                              #counter for the number of "A's" in a -LINE-
        words = line.split()                    #split the line into a list of words
        num_words = num_words + len(words)

        for word in words:                      #step through each word in the list of words
            
            num_yY = 0                          #counter for the number of "Y's" in a WORD
            num_zZ = 0                          #counter for the number of "Z's" in a WORD
            for letter in word:
                if letter in alphabet:
                    num_letters = num_letters + 1
                if letter in yY:                
                    num_yY = num_yY + 1         #Keep track of the number of Y's in the WORD
                if letter in zZ:
                    num_zZ = num_zZ + 1         #Keep track of the number of Z's in the WORD
                if letter in aA:
                    num_aA = num_aA + 1         #Keep track of the number of A's in the -LINE-

            if num_yY >=1 and num_zZ >=1 and len(word) >= 10:
                long_words.append(word)         #Add the word to a list if it meets the criteria
        if num_aA == 0:
            lines_no_As.append(line)            #Add the line to a list if it meets the criteria

    counts = num_lines, num_letters, num_words  #Put the counts in a list, only because i felt like it.

    print('\n\n\n')
    print('LINES WORDS LETTERS____________________________________________________________________________________________________')
    print(counts)
    print('\n\n\n')
    print('LONG WORDS w Ys and Zs_________________________________________________________________________________________________')
    print(long_words)
    print('\n\n\n')
    print('LINES WITH NO As_______________________________________________________________________________________________________')
    print(lines_no_As)


    
scan_a_file()

