import csv, math

passengerid = [] #0
survived = [] #1
pclass = [] #2
pname  = [] #3
gender = [] #4
age    = [] #5
sibsp  = [] #6
parents= [] #7
ticket = [] #8
fare   = [] #9
lista  = []

def read_data(infile):
    csv.register_dialect('myDialect',delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
    with open(infile, 'r') as f:
        reader = csv.reader(f, dialect='myDialect')
        header = f.readline().strip() #skip over header line        
        print(header)
        for row in reader:
            if row[5] != '':
                if float(row[5]) < 17:
                    age.append('Child')
                    newage = 'Child'
                elif float(row[5]) < 25:
                    age.append('Young Adult')
                    newage = 'Young Adult'
                elif float(row[5]) < 60:
                    age.append('Adult')
                    newage = 'Adult'
                else:
                    age.append('Aged')
                    newage = 'Aged'
            else:
                if 'Master' in row[3]:
                    age.append('Child')
                    newage = 'Child'
                elif 'Miss' in row[3] and float(row[6]) > 0 and float(row[7]) > 0:
                    age.append('Child')
                    newage = 'Child'
                else:
                    continue  #could not resolve an age so skip this row entirely and 'contiue' to next row
                    #age.append('Bad Row')
            
            passengerid.append(row[0])
            survived.append(row[1])
            pclass.append(row[2])
            pname.append(row[3])
            gender.append(row[4])
            sibsp.append(row[6])
            parents.append(row[7])
            ticket.append(row[8])
            fare.append(row[9])
            lista.append((row[0],row[1], row[2], row[3], row[4], newage, row[6], row[7], row[8], row[9]))
    
 #   for row in lista:
 #       print(row)
    return lista

    #print(lista)


train_data = read_data('train.csv')


def entrophy(data,col):
    d = dict()
    total = 0
    for row in data:
        if row[col] not in d:
            d[row[col]] = 1
        else:
            d[row[col]] += 1
        total = total + 1

    entro = -(d['0']/total)*math.log2(d['0']/total) - (d['1']/total)*math.log2(d['1']/total)
    
    print(d['0'], d['1'], total)
    print(entro)
    return entro

#entro_set = entrophy(train_data, 1)

def entrophytwo(data,col1,col2):
    d = dict()
    q = dict()
    total = 0
    for row in data:
        pairx = str(row[col1]+row[col2])

        if    (row[col1],row[col2]) not in d:
            d[(row[col1],row[col2])] = 1
        else:
            d[(row[col1],row[col2])] += 1
        total = total + 1
        
        #---------------------------------------
        if (row[col2]) not in q:
            if row[col1] == '0':
                q[row[col2]] = [1,0]
            else:
                q[row[col2]] = [0,1]
        else:
            if row[col1] == '0':
                q[row[col2]][0] += 1
            else:
                q[row[col2]][1] += 1
        


    print(d)
    print(q)
    p = dict()
    for i in d:
    #     if d[1] not in p:
    #         p[d[1]] = 
       
        print(i[0],i[1], d[i])
        
 #       print(row)
    entro = 1 # -(d['00']/total)*math.log2(d['00']/total) - (d['11']/total)*math.log2(d['11']/total)
    
#    print(d['00'], d['11'], total)
#    print(entro)
    return entro

entro_set = entrophytwo(train_data, 1,4)






