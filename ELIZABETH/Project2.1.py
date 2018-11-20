import csv, math

#  i dont use these lists, they just help me remember what columns go to which data elements
passengerid = [] #0 Skip this when reading data in
survived = [] #1   Keep  1  
pclass = [] #2     Keep? 2
pname  = [] #3 Skip
gender = [] #4     Keep  3
age    = [] #5     Keep  4
sibsp  = [] #6 Skip
parents= [] #7 Skip
ticket = [] #8 Skip
fare   = [] #9     Keep  5
lista  = [] #  i clean up the data in this list


#---------------------------------------------------------------------------------------
# first task, data cleanup, make age "bins", toss data with no age value
#---------------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------------
# second task, calculation entrophy of the target data which is in column 1 = survived
#---------------------------------------------------------------------------------------
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
    
    print('Died',d['0'], 'Survived', d['1'],'Total', total)
    print('Entrophy', entro)
    return entro

entro_set = entrophy(train_data, 1)

#---------------------------------------------------------------------------------------
# third task, calculate entrophy for the interaction between survival and 
# an attribute of the passenger.  I pass in two columns from the data set.
#---------------------------------------------------------------------------------------

def entrophytwo(data,col1,col2):
    d = dict()
    total = 0
    for row in data:
        total = total + 1
        if (row[col2]) not in d:
            if row[col1] == '0':
                d[row[col2]] = [1,0]
            else:
                d[row[col2]] = [0,1]
        else:
            if row[col1] == '0':
                d[row[col2]][0] += 1
            else:
                d[row[col2]][1] += 1

    print("\nThe following is a list of [died,survived] pairs by attribute.")    
    print (d)  
    print("\n")

    entro = 0
    for value in d:
        #print(value, d[value][0], d[value][1])
        prob = (d[value][0] + d[value][1])/total
        valtot = (d[value][0] + d[value][1])
        entro += prob*(-(d[value][0]/valtot)*math.log2(d[value][0]/valtot) - (d[value][1]/valtot)*math.log2(d[value][1]/valtot))
    return entro

entro_set = entrophytwo(train_data, 1,4)
print('Entrophy', entro_set)

#print(header)



