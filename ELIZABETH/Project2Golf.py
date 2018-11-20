import csv
lista = []
def read_data(infile):
    csv.register_dialect('myDialect',delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
    with open(infile, 'r') as f:
        reader = csv.reader(f, dialect='myDialect')
        f.readline().strip() #skip over header line        
        for row in reader:
            print(row)
            lista.append(row)


read_data('golf.csv')