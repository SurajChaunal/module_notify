#!/usr/bin/env python
import os.path
from operator import itemgetter
import sys

list1=[]
separator="***************\n"
length=[]
f = open("dat.txt", 'r')
sample=open("program.py",'r')
wt=open("mapper.py","w")
for line in sample:
    if line==separator:
        for l in f:
            wt.write('list1.append("'+l.rstrip('\n').rstrip('\r')+'")\n')
            wt.write('length.append('+str(len(l.rstrip('\n').rstrip('\r')))+')\n')
    else:
        wt.write(line)
wt.close()
sample.close()
f.close()
os.system("echo finish")
