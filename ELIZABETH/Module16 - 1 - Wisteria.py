
def scan_a_file():
    fin = open('wisteria.txt', encoding='utf-8')
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_lines   = 0
    num_words   = 0
    num_letters = 0
    num_longwords = 0
    long_words  = []

    for line in fin:
        line = line.strip()
        num_lines = num_lines + 1
        
        words = line.split()                    #split the line into a list of words
        
        for word in words:                      #step through each word in the list of words
            if not (word.startswith('www') or word.startswith('http')):
                num_words = num_words + 1
                stripped_word = '' 
                for letter in word:
                    if letter in alphabet:
                        num_letters = num_letters + 1
                        stripped_word = stripped_word + letter
                    if len(stripped_word) >= 10:
                        long_words.append(stripped_word)
                        num_longwords = num_longwords +1
        

    #print(long_words)
    print('Lines, Words, Letters, Long Words-------------------------------------------------------------------------\n')
    print(num_lines,num_words, num_letters, num_longwords)

scan_a_file()

