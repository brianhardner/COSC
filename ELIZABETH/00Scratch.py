
""" 

global_offset = ord('A')
global_length = ord('Z')-ord('A')+1
def change(letter, pwd):
    return chr( (ord(letter)+ord(pwd)-2*global_offset)%global_length+global_offset)

def unchange(letter, pwd):
    return chr( (ord(letter)-ord(pwd)+global_length)%global_length + global_offset)

print(change("E","L"))
print(unchange("P","L"))



ord(‘V’) = (ord(secret)-ord(‘A’)+ord(‘E’)-ord(‘A’))%26+ord(‘A’) 

 """


xx = ()
names = ("Albert", "Bill", "Carl", "Dave")
grades = ("A","B","C","D")
school = ("MPS","DHS","GBN","GBS")

zip(names, grades, school)

x = list(zip(names, grades, school))

print('pause')
for i in range(len(names)):
    print(names[i], grades[i], school[i])

for i in range(len(x)):
    print(x[i][0],x[i][1],x[i][2])
    
    