


def weather_data():
    fin = open('abq10001.dat.txt')
    observations = 0
    sum_of_dw_psp = 0
    station_name = fin.readline()
    station_info = fin.readline()
    for line in fin:
        observations = observations + 1
        line = line.strip()
        field = line.split()
        sum_of_dw_psp = sum_of_dw_psp + float(field[8])

    print('\n\n\n________________________________________________________________________________')
    print('Station: ', station_name, '  Info: ', station_info)
    print('Average DW_PSP: Sum:',round(sum_of_dw_psp,2),' Obs: ', observations, 'Mean: ',round(sum_of_dw_psp / observations,2))
    print('________________________________________________________________________________')
    
weather_data()