import os


def list_files(dir_name):
    files = os.listdir(dir_name)
 
    for my_file in files:
        print(my_file, os.path.getsize(dir_name+"/"+my_file))

#list_files('example')

def process_a_file(file_name):
    with open(file_name,'r') as infile:
        suma = 0
        nr_lines = 0
        for line in infile:
            nr_lines+=1
            array = line.split(',')
            suma+= float(array[1])/float(array[0])
        print(suma/nr_lines)
        return suma/nr_lines

process_a_file('example/results0.csv')


def process_files(dir_name):
    files = os.listdir(dir_name)
    for my_file in files:
        if my_file.endswith('.csv'):
            print(my_file, process_a_file('Example/{}'.format(my_file)))

#process_files('example')

