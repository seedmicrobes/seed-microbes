#! /usr/bin/env python3

import sys
import os

def main():
    counter = 1
    fastqfile = open(sys.argv[1], 'r')
    if not os.path.exists('newheader'):
        os.makedirs('newheader')
    newfile = open('newheader/'+fastqfile.name, 'w')
    for line in fastqfile:
        if counter > 4:
            counter = 1
        if line[0] == '@' and counter == 1:
            line =  line[:-3]
            run = line.split("-")[1]
            line = line.split("-")[0]
            sample = line.split("_")[0]
            seq = line.split("_")[1]
            line = sample+'.'+run+'_'+seq+'\n'
        newfile.write(line)
        counter = counter + 1  
    newfile.close()
    fastqfile.close()       
        

if __name__ == "__main__":
    main()        
