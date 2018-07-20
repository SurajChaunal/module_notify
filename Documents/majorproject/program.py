#!/usr/bin/env python
import os.path
from operator import itemgetter
import sys

list1=[]
length=[]

***************

for text in sys.stdin:
	
########################## first gene finding code ############################
	pat=list1[0]
	m=len(pat)
	n=len(text)

	arr=[]

	for i in range(0,256):
    		arr.append(-1)

	for i in range(0,m):
   	 	arr[ord(pat[i])]=i
    
	s=0

	while (s<=(n-m)):
    		j=m-1
    		while j>=0 and  pat[j]==text[s+j]:
        		j=j-1
    
    		if j<0:
        		print '%s\t%s' %('1','1')
			
        		if s+m<n:
            			s=s+(m-arr[ord(text[s+m])])
        		else:
            			s=s+1
        
    		else:
       
        		s=s+(max(1,j-arr[ord(text[s+j])]))


################## second gene  finding code ###########################
	pat=list1[1]
        m=len(pat)
        n=len(text)

        arr=[]

        for i in range(0,256):
                arr.append(-1)

        for i in range(0,m):
                arr[ord(pat[i])]=i
    
        s=0

        while (s<=(n-m)):
                j=m-1
                while j>=0 and  pat[j]==text[s+j]:
                        j=j-1
    
                if j<0:
                        print '%s\t%s' %('2','1')
			
                        if s+m<n:
                                s=s+(m-arr[ord(text[s+m])])
                        else:
                                s=s+1

                else:

                        s=s+(max(1,j-arr[ord(text[s+j])]))


################# third gene finding code #########################

	pat=list1[2]
        m=len(pat)
        n=len(text)

        arr=[]

        for i in range(0,256):
                arr.append(-1)

        for i in range(0,m):
                arr[ord(pat[i])]=i
    
        s=0

        while (s<=(n-m)):
                j=m-1
                while j>=0 and  pat[j]==text[s+j]:
                        j=j-1
    
                if j<0:
                        print '%s\t%s' %('3','1')
			
                        if s+m<n:
                                s=s+(m-arr[ord(text[s+m])])
                        else:
                                s=s+1

                else:

                        s=s+(max(1,j-arr[ord(text[s+j])]))



