#!/usr/bin/python

import Tkinter
import getpass
import sys
import subprocess
import telnetlib
import os.path
from Tkinter import *
import os
top = Tk()
top.geometry("620x300")
# Code to add widgets will go here...
def start_cluster():
	#os.system("su hduser;open")
	#os.system("open")
	os.system("$HADOOP_HOME/sbin/start-all.sh")
	os.system("echo finish")
def stop_cluster():
	#os.system("su hduser")
	#os.system("open")
	os.system("$HADOOP_HOME/sbin/stop-all.sh")
def execute():
	wt=open("dat.txt","w")
	print len(e1.get())
	wt.write(e1.get()+'\n')
	print len(e2.get())
	wt.write(e2.get()+'\n')
	print len(e3.get())
	wt.write(e3.get()+'\n')
	wt.close()
	os.system("python mpcreator.py")
	os.system("hadoop fs -rm -r word/output/*")
	os.system("$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input word/input/chromo1.txt -output word/output/def")
	os.system("hadoop fs -cat /user/hduser/word/output/def/part-00000 > tmpout.txt")
	ra = open("tmpout.txt",'r')
	s=""
	for i in ra:
		s=s+i+'\n'
	text.insert(INSERT, s)
def check():
	#os.system("su hduser")
	#os.system("open")
	os.system("jps")



start = Tkinter.Button(top, text ="Start Cluster", command = start_cluster)
stop = Tkinter.Button(top, text ="Stop Cluster", command = stop_cluster)
run = Tkinter.Button(top, text ="Execute", command = execute)
check = Tkinter.Button(top, text ="jps", command = check)

text = Text(top,height=10,width=50)
text.grid(row=0,column=2)
out = Label(top, text="OUTPUT")
l1 = Label(top, text="Gene 1")
l2 = Label(top, text="Gene 2")
l3 = Label(top, text="Gene 3")
e1 = Entry(top, bd =3,width=50)
e2 = Entry(top, bd =3,width=50)
e3 = Entry(top, bd =3,width=50)

out.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)


start.grid(row=6,column=1)
stop.grid(row=6,column=4)
check.grid(row=7, column =1)
run.grid(row=7,column = 4) 
top.mainloop()

