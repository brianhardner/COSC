with open('avocado.csv','r') as infile, open('avocadoNEW.dat','wt') as outfile:
    for row in infile:
        fields = row.split(',')
        #print(fields[1],fields[2],fields[11],fields[13])
        outfile.write('{}  {}  {}  {}\n'.format(fields[1].strip(),fields[2].strip(),fields[11].strip(),fields[13].strip()))


