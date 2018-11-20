import random
global rand_index, wordlist, seen_list, letter

""" Before we can start, we need to have a source for words to be guessed. On the internet, you
can find a “English word list” by Lawles that you can download. Our first task is to remove
some words that do not fit the hangman game. Our first task is to write a Python script that
takes the words in the Lawles file and writes them into another file, called “vocabulary.txt”,
unless the word contains a hyphen, a parenthesis, or is too small, i.e. has a length of less than
five letters. """
def sanitize_wordlist():
    fin = open('lawler.txt', encoding='utf-8')
    outfile = open('vocabulary_good.txt','wt')
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for line in fin:
        line = line.strip()
        words = line.split()                    #split the line into a list of words
        for word in words:                      #step through each word in the list of words
            good_word = '' 
            for letter in word:
                if letter in alphabet:
                    good_word = good_word + letter
            if len(good_word)>=5:
                outfile.write(good_word+'\n')

#sanitize_wordlist()


""" After we created our file, we write a function def get_random_word(): that randomly
selects a word from “vocabulary.txt”. The function opens the file and reads all words line by
line into a list.
"""
def read_wordlist():
    fin = open('vocabulary_good.txt')
    vocab_list = []
    for line in fin:
        line = line.strip()
        words = line.split()                    #split the line into a list of words
        for word in words:
            vocab_list.append(word)
    return vocab_list        

#wordlist = read_wordlist()
#print(wordlist)

""" We then use the function random.randint(0, len(lista)-1) to randomly
select an index of an element in the list and then print out the word in the list at this index. If
we were anticipating playing Hangman incessantly, then we might want to create the list of
words once per session and select the word out of the list separately for each round of game.  """
def get_random_word(lista):
    return lista[(random.randint(0, len(lista)-1))]

#random_word = get_random_word(wordlist)
#random_word = list(random_word)
#print (random_word)


""" Write a function def get_letter(seen_list): that uses
a list of already seen letters. It uses an infinite loop. In each
iteration, the program asks the user to enter a letter, takes the
first letter of the input, and converts the letter to lower case. If
the letter is not in the list of already seen letters, it accepts the
letters and returns it (jumping out of the infinite loop by this).
Otherwise, it just complains. The drawing on the left shows
the control flow, but frankly, it is more complicated than the
Python function """

seen_list = []
def get_letter(lista):
    guess = input('Select a letter: ')
    while guess in lista:
        guess = input('You tried that one already.  Try again: ')
        
    return guess

#letter = get_letter(seen_list)

""" Checking for Success
If the user enters a letter, three cases arise: First, the letter
has already been entered. In this case, the previously
described getting-a-letter function handles the prompting for
another letter. Second, the letter is new, but not in the word.
In the main function, this results in incrementing the number of errors. Third, the letter is new
and it is in the word. The main function will then check whether the word has been guessed.
To do this, it is easier to write a function def success(word, seen_list) that returns
True if all of the letters in the argument word (containing the word to be guessed) are in the
seen_list, containing all the letters that the user has guessed so far. The function just
passes through the letters in word. If a letter is not in the seen_list, then it returns False. If
however all the letters are in the seen_list, then it returns True. """

def success(word, lista):
    for letter in word:
        if letter not in lista:
            return False
    return True

#x = success(['a','b','c'], ['a','b','c'] )
#x = success(['a','b','c'], ['a','b','x'] )
#print(x)



""" Like good software engineers, we have divided the task into small modules. In a bottom-up
manner, we now create the main function, called def play_hangman( ). The function
maintains a state consisting of the list of seen letters, the secret word, and the number of
errors.

 It then enters the main loop. We display the secret word (initially with only underscores)
and ask for a new letter. The new-letter function already handles instances of the letter entered
by the user having been seen before. There are now two possibilities: First, the new letter is
not in the word. In this case, we increment the number of errors and inform the user with a
“Sorry”. We also check whether the number of errors is too large, in which case we inform the
user, print out the secret word and return from the play_hangman function, or alternatively,
draw the hangman. Second, the new letter is in the word. We check whether the user has
guessed the word. If yes, we congratulate, otherwise, we display the hangman and the secret
word (minus the non-guessed letters). Some of this functionality can be embedded in the test
for the while loop or you can have an infinite while True loop.  """



#### ---- MAIN Hangman Routine (not written as a proceedure, but could be)
#sanitize_wordlist()
wordlist = read_wordlist()
random_word = get_random_word(wordlist)
random_word = list(random_word)
guess_word = '-'*len(random_word)
guess_word = list(guess_word)

bad_guesses = 0

while bad_guesses < 6:
    guess_letter = get_letter(seen_list)
    if guess_letter in random_word:
        letter_num = 0
        for letter in random_word:
            if letter == guess_letter:
                guess_word[letter_num] = letter
            letter_num = letter_num + 1
    else:
        bad_guesses = bad_guesses + 1
    
    seen_list.append(guess_letter)
    
    winner = success(random_word, seen_list)
    if winner == True:
        print('You Win!!!')
        break
    elif bad_guesses > 5:
        print('You Lose')      
    #print(random_word, guess_word,bad_guesses, seen_list)


    print('Word we are guessing: {}\nLetters we filled in: {}\nNumber of bad guesses: {}\nGuessed letters:      {}\n'.format(random_word, guess_word,bad_guesses, seen_list))

