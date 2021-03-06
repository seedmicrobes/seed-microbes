#! /usr/bin/env python3
# remultiplex.py [1] [2] [3]
# arg[1] input file
# arg[2] concatenated filename
# arg[3] run number
# Recombines all files and changes header to following format:
# @Sample[Sample#].[Run#]_Read[Sequence#]

import sys


def main():
    counter = 1
    index=1
    fastqfile = open(sys.argv[1], 'r')
    concat = open(sys.argv[2], 'a')
    run = '-'+str(sys.argv[3])
    fastqname = fastqfile.name
    ID = fastqname.split("_")[0]
    for line in fastqfile:
        if counter > 4:
            counter = 1
        if line[0] == '@' and counter == 1:
            line =  '@Sample'+str(ID)+"."+run+"_Read"+str(index)+"\n"
            index = index + 1
        concat.write(line)
        counter = counter + 1  
    concat.close()
    fastqfile.close()       
        

if __name__ == "__main__":
    main()        
