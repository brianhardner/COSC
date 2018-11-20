import csv, math

#  i dont use these lists, they just help me remember what columns go to which data elements
# passengerid = [] #0 Skip this when reading data in
# survived = [] #1   Keep  0  
# pclass = [] #2     Keep? 1
# pname  = [] #3 Skip
# sex    = [] #4     Keep  2
# age    = [] #5     Keep  3
# sibsp  = [] #6 Skip
# parents= [] #7 Skip
# ticket = [] #8 Skip
# fare   = [] #9     Keep  4
# lista  = [] #  i clean up the data in this list
# splitlist = []


#---------------------------------------------------------------------------------------
# first task, data cleanup, make age "bins", toss data with no age value
#---------------------------------------------------------------------------------------
def read_data(infile):
    lista  = []
    csv.register_dialect('myDialect',delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
    with open(infile, 'r') as f:
        reader = csv.reader(f, dialect='myDialect')
        #header = f.readline().strip() #skip over header line        
        #print(header)
        row_count = 1
        for row in reader:
            if row_count == 1:
                lista.append((row[1], row[2], row[4], row[5], row[9]))        #this will write the header row
            else:    
                if row[5] != '':                #create Age Bins
                    if float(row[5]) < 17:
                        newage = 'Child'
                    elif float(row[5]) < 25:
                        newage = 'Young Adult'
                    elif float(row[5]) < 60:
                        newage = 'Adult'
                    else:
                        newage = 'Aged'
                else:
                    if 'Master' in row[3]:
                        newage = 'Child'
                    elif 'Miss' in row[3] and float(row[6]) > 0 and float(row[7]) > 0:
                        newage = 'Child'
                    else:
                        continue  #could not resolve an age so skip this row entirely and 'contiue' to next row
                        #age.append('Bad Row')
                
                if float(row[9]) < 50:
                    newfare = 'Low Fare'
                elif float(row[9]) < 90:
                    newfare = 'Moderate Fare'
                else:
                    newfare = 'High Fare'

                lista.append((row[1], row[2], row[4], newage, newfare))    #this will write the data rows
            row_count +=1
#    for row in lista:
#        print(row)
    return lista

train_data = read_data('train.csv')

#---------------------------------------------------------------------------------------
# second task, calculation entrophy of the target data which is in column 1 = survived
#---------------------------------------------------------------------------------------
def entrophy(data,col):
    d = dict()
    total = 0
 
    for row in data[1:]:  #use [1:] to skip over first row as that is the header
        if row[col] not in d:
            d[row[col]] = 1
        else:
            d[row[col]] += 1
        total = total + 1
    entro = -(d['0']/total)*math.log2(d['0']/total) - (d['1']/total)*math.log2(d['1']/total)
    

    print('Died',d['0'], 'Survived', d['1'],'Total', total)
    print('Total Entrophy', entro)
    return entro


#---------------------------------------------------------------------------------------
# third task, calculate entrophy for the interaction between survival and 
# an attribute of the passenger.  I pass in two columns from the data set.
#---------------------------------------------------------------------------------------

def entrophytwo(d):
    total = 0
    entro = 0
    for value in d:
        total += (d[value][0] + d[value][1])

    for value in d:
        #print(value, d[value][0], d[value][1])
        if d[value][0] == 0 or d[value][1] ==0:
            print('this is a leaf node',value)
        else:
            prob = (d[value][0] + d[value][1])/total
            valtot = (d[value][0] + d[value][1])
            entro += prob*(-(d[value][0]/valtot)*math.log2(d[value][0]/valtot) - (d[value][1]/valtot)*math.log2(d[value][1]/valtot))
    return entro


def histogram(data,col1,col2):
    d = dict()

    for row in data[1:]:        # start from [1:] to skip the header
        
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

 #   print("\nThe following is a list of [died,survived] pairs by attribute.")    
 #   print (d)  
 #   print("\n")
    return d


def leaf_status(d):
    for value in d:
        if (d[value][0]/(d[value][0] + d[value][1]) >=.8 
        or d[value][1]/(d[value][0] + d[value][1]) >= .8):
            print('this is a leaf node',value)


def find_best_gain(data):
    best_gain = 0
    total_entro = entrophy(data, 0)        
    for i in range (1,(len(data[0]))):
        d = histogram(data,0,i)
        leaf_status(d)
        entro_set = entrophytwo(d)
        gain = total_entro - entro_set
        if gain >= best_gain:
            best_gain = gain
            best_node = data[0][i]
            best_node_number = i
        #print('Entrophy for', data[0][i],"is", entro_set)  #,'gain is',gain)
    print('Best Gain is ',best_node,best_gain,'in column',best_node_number)
    
    d = histogram(data,0,best_node_number) #find the values to split on (e.g. male and female)
    
    for value in d:
        print('LEAF:',value)
        splitlist = []
        row_count = 1
        for row in data:        #pass thru this set of data skipping over the leaf field (best node number)
            if row_count == 1:
                newrow = row[:best_node_number]+row[best_node_number+1:]  #new row is w/o leafed field header
                splitlist.append(newrow)
            else:
                if row[best_node_number] == value:
                    newrow = row[:best_node_number]+row[best_node_number+1:] #new row is w/o leafed field data
                    splitlist.append(newrow)
            row_count += 1
        
 #       for row in splitlist:
 #           print(row)
        print('pause')
        find_best_gain(splitlist) 
        #print(value, len(splitlist))
       
find_best_gain(train_data)


#---------------------------------------------------------------------------------------
# this starts task 7.  i skipped over the others so i could get to the decision tree
# part of the problem.  this first function goes through the list of attributes, calculates
# entrophy for the attribute pair (e.g. Age & Survived, Gender & Survived, etc.) and 
# subtracts that from the entrophy of [Survived] by itself.  It then fineds that attribute
# that provides the best information "gain".  This will represent our first / next 
# branch in the decision tree.
#---------------------------------------------------------------------------------------




