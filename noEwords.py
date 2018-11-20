def has_no_e(letter_lookup):
    total_words = 0
    found_words = 0
    fin = open('words.txt')
    for line in fin:
        total_words = total_words+1
        word = line.strip()
        if letter_lookup in word:
            found_words = found_words+1
            ##print(word)
    
    return(found_words,total_words)        
print('Words with e')
a=has_no_e('e')
print(a[0],a[1], round(a[0]/a[1],2))