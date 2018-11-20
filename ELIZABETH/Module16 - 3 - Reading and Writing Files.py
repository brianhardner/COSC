import os

def process_a_file(file_name):
    with open(file_name,'r') as infile, open(file_name[:len(file_name)-4]+'.dat','wt') as outfile:
        for line in infile:
            array = line.split(',')
            for afield in array:
                outfile.write('{} '.format(afield.strip()))
                print(afield)
            outfile.write('\n')


def process_files(dir_name):
    files = os.listdir(dir_name)
    for my_file in files:
        if my_file.endswith('.csv'):
            process_a_file('Example/{}'.format(my_file))

process_files('example')