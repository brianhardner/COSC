import csv

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
    for row in lista:
        i=3
        h1 = row[:i]+row[i+1:]
        print(row,h1)
    
    return lista

train_data = read_data('train.csv')
