# # # # # # #
### LAB 7 ###
# # # # # # #

#---------ALICE COUNTS----------

def alice():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'   # define a list of valid letters against which 
                                                                        # we will evaluate characters in words to see if they are "good"
    long_words=[] 
    with open('alice.txt','r') as f:
        for line in f:
            if 'y' in line and 'z' in line:
                print('YZ Line  |', line)
            if 'ing'in line:
                print('ING Line |', line)
              
            for word in line.split():
                clean_word = ''                 #make a place to hold all of the good letters of a word as compard to the alphabet variable defined above
                for letter in word:
                    if letter in alphabet:      #this gets rid of characters you dont want
                        clean_word = clean_word + letter
                if len(clean_word)>8:
                    long_words.append(clean_word)

        print('LONG WORDS______________________________________________________________________________________')
        print(long_words)


alice()