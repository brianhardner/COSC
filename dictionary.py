
def make_word_list():
    fin = open('words.txt')
    count = 0
    for line in fin:
        count = count + 1
        word = line.strip()
        word_list[word] = count

def reverse_lookup(d,v):
    for k in d:
    ##    print(d[k], k , v)
        if d[k] == v:
            return k
    raise LookupError()

word_list = dict()
make_word_list()

print(len(word_list))
print(word_list.get ('aa',0))
print(word_list.get ('aah',0))
print(word_list.get ('zymurgies',0))
print(word_list.get ('zymurgy',0))


print(reverse_lookup(word_list,1))
print(reverse_lookup(word_list,2))
print(reverse_lookup(word_list,100000))
print(reverse_lookup(word_list,113808))



