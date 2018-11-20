def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)
        d[c] = d[c]+ 1
    return d

def print_hist(h):
    for c in sorted(h):
        print(c,h[c])

h = histogram('AAAbrontosaurusxxxxxxx')
#print_hist(h)


print(h)

