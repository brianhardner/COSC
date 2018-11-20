# # # # # # #
### LAB 7 ###
# # # # # # #

#---------IRIS SUMS using a Dictionary (this is tricky)----------

def iris():
    slength = dict() #this are dictionaries that will hold sums for each of the flower types
    swidth  = dict()
    plength = dict()
    pwidth  = dict()
    counter = dict()

    
    with open('iris.csv','r') as f:
        x = f.readline() #.strip()
        #x = x.strip()
        for row in f:
            field = row.split(',')
            flower = field[5].strip('\n')
            if flower not in slength:
                slength[flower] = float(field[1])
                swidth[flower]  = float(field[2])
                plength[flower] = float(field[3])
                pwidth[flower]  = float(field[4])
                counter[flower] = 1
            else:
                slength[flower] += float(field[1])
                swidth[flower]  += float(field[2])
                plength[flower] += float(field[3])
                pwidth[flower]  += float(field[4])
                counter[flower] += 1

        print(slength,'\n')
        print(swidth,'\n')
        print(plength,'\n')
        print(pwidth,'\n')
        print(counter,'\n')

    for flower in slength:
        print(flower,slength[flower]/counter[flower], swidth[flower]/counter[flower], plength[flower]/counter[flower], pwidth[flower]/counter[flower])

iris()

# OUR TABLE OF DATA
# field[0]  Id                  
# field[1]  SepalLengthCm               s_length
# field[2]  SepalWidthCm                s_width
# field[3]  PetalLengthCm               p_length
# field[4]  PetalWidthCm                p_width
# flower  Species e.g. Iris-setosa    this will be the dictionary key in the ()'s