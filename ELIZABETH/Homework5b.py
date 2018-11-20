


def number2letters(anum):
    phonenum = list(anum)
    two = ['A','B','C']
    three = ['D','E','F']
    four = ['G','H','I']
    five = ['J','K','L']
    six = ['M','N','O']
    seven = ['P','Q','R','S']
    eight = ['T','U','V']
    nine = ['W','X','Y','Z']
    ListofLetters = [two] + [three]+[four]+[five]+[six]+[seven]+[eight]+[nine]
    ListofNumbers = [2,3,3,4,5,6,7,8,9]

    for c in ListofLetters[int(phonenum[0])-2]:
        for d in ListofLetters[int(phonenum[1])-2]:        
            for e in ListofLetters[int(phonenum[2])-2]:
                for f in ListofLetters[int(phonenum[3])-2]:
                    for g in ListofLetters[int(phonenum[4])-2]:           
 #                       for h in ListofLetters[int(phonenum[5])-2]:            
 #                           for i in ListofLetters[int(phonenum[6])-2]:            
 #                               for j in ListofLetters[int(phonenum[7])-2]:
                                    print(c,d,e,f,g)

#    print(ListofNumbers[0],ListofLetters[0][0])
#    print(ListofNumbers[0],ListofLetters[0][1])
#    print(ListofNumbers[0],ListofLetters[0][2])


number2letters('27426')
            
