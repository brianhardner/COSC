def find_longwords(Num_Chars):
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) >= Num_Chars:
            print(word)
            
print('Words with 20 Chars')
find_longwords(20)
print('')