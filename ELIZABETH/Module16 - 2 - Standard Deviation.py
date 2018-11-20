import os

def process_a_file(file_name):
    with open(file_name,'r') as infile:
        
        ## Calculat the Average of the second field
        suma = 0
        nr_lines = 0
        field_two  = []                         #populate a list with the values in field 2 (array [1]) below
                                                #this way we wont have to read the file again
        for line in infile:
            nr_lines+=1
            array = line.split(',')
            suma+= float(array[1])
            field_two.append(float(array[1])) 
        avga = suma / nr_lines                  
        
        #Calculate the Average of the Errors Squared
        sumE = 0    #Sum of Errors Squared
        avgE = 0    #Average of sumE
        std_dev = 0 #Square Root of avgE
        for row_value in field_two:
            sumE+= (row_value-avga)**2
        avgE = sumE / nr_lines
        std_dev = avgE**.5 
        
        print(file_name, avga, std_dev)
        

def process_files(dir_name):
    files = os.listdir(dir_name)
    for my_file in files:
        if my_file.endswith('.csv'):
            process_a_file('Example/{}'.format(my_file))

process_files('example')