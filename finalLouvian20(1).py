# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 18:57:05 2017

@author: prem
"""
import math
import unittest
from pylouvain import PyLouvain
import numpy

pyl = PyLouvain.from_file("/home/pk/Python Wd/Python wd_old/Edge_List_t+0.txt")
partition1, q = pyl.apply_method()
        
pyl = PyLouvain.from_file("/home/pk/Python Wd/Python wd_old/Edge_List_t+4.txt")
partition2, q = pyl.apply_method()

pyl = PyLouvain.from_file("/home/pk/Python Wd/Python wd_old/Edge_List_t+8.txt")
partition3, q = pyl.apply_method()

pyl = PyLouvain.from_file("/home/pk/Python Wd/Python wd_old/Edge_List_t+12.txt")
partition4, q = pyl.apply_method()

pyl = PyLouvain.from_file("/home/pk/Python Wd/Python wd_old/Edge_List_t+16.txt")
partition5, q = pyl.apply_method()

len(partition1)
print partition1[1]

# Matching

#a is matching values for all combinations t1 and t2
a1=[];
for i in range(len(partition1)):
    for j in range(len(partition2)):
        #print i, j
        #print (len(set(partition1[i]).intersection(partition2[j]))/float(len(partition1[i])))
        a1.append(( i, j, len(set(partition1[i]).intersection(partition2[j]))/float(len(partition1[i]))))
        print a1

a2=[];    
for i in range(len(partition2)):
    for j in range(len(partition3)):
        #print i, j
        a2.append(( i, j, len(set(partition2[i]).intersection(partition3[j]))/float(len(partition2[i]))))
        print a2

a3=[];        
for i in range(len(partition3)):
    for j in range(len(partition4)):
        #print i, j
        a3.append(( i, j, len(set(partition3[i]).intersection(partition4[j]))/float(len(partition3[i]))))
        print a3

a4=[];        
for i in range(len(partition4)):
    for j in range(len(partition5)):
        #print i, j
        a4.append(( i, j, len(set(partition4[i]).intersection(partition5[j]))/float(len(partition4[i]))))
        print a4

#Matrix after Louvian
list1=[];
list1.append(partition1);
list1.append(partition2);
list1.append(partition3);
list1.append(partition4);
list1.append(partition5);
list1a=numpy.asarray(list1);

#Postimage
x=len(a1)/len(partition2);   
M1=[];
for i in range(len(a1)):
    M1.append(a1[i][2]);
import numpy
M1a=numpy.asarray(M1);
M1s=numpy.split(M1a,x);
max1=numpy.amax(M1s, axis=1); #max matching value of t2 partitions with t1 partitions              
print numpy.amax(M1s, axis=1);
#print max1;
#print numpy.argmax(M1s, axis=1);
imax1=numpy.argmax(M1s, axis=1);#index of t2 with max matching
                  

x=len(a2)/len(partition3);   
M2=[];
for i in range(len(a2)):
    M2.append(a2[i][2]);
import numpy
M2a=numpy.asarray(M2);
M2s=numpy.split(M2a,x);
max2=numpy.amax(M2s, axis=1);
print numpy.amax(M2s, axis=1);
#print max1;
#print numpy.argmax(M2s, axis=1);
imax2=numpy.argmax(M2s, axis=1);
                  
x=len(a3)/len(partition4);   
M3=[];
for i in range(len(a3)):
    M3.append(a3[i][2]);
import numpy
M3a=numpy.asarray(M3);
M3s=numpy.split(M3a,x);
max3=numpy.amax(M3s, axis=1);
print numpy.amax(M3s, axis=1);
#print max1;
#print numpy.argmax(M3s, axis=1);
imax3=numpy.argmax(M3s, axis=1);
                  
x=len(a4)/len(partition5);   
M4=[];
for i in range(len(a4)):
    M4.append(a4[i][2]);

M4a=numpy.asarray(M4);
M4s=numpy.split(M4a,x);
max4=numpy.amax(M4s, axis=1);
print numpy.amax(M4s, axis=1);
#print max1;
#print numpy.argmax(M4s, axis=1);
imax4=numpy.argmax(M4s, axis=1);
                  
#Matrix after pre-Snapshot

#max matching index
list2=[];
list2.append(imax1);
list2.append(imax2);
list2.append(imax3);
list2.append(imax4);
list2a=numpy.asarray(list2);
            
#max matching value            
list3=[];
list3.append(max1);
list3.append(max2);
list3.append(max3);
list3.append(max4);
list3a=numpy.asarray(list3);
                    
#Thresholdiing and Union
thres=0.58;

t1list2=list2[:];
for i in range(len(list2a)):
    for j in range(len(list2a[i])): 
        if list3a[i][j]<thres:
            t1list2[i][j]=100;
print t1list2;
    
#Writing time value matrix for 5 snapshots:
traverse=[];
traverse.append(len(list1[0]));
traverse.append(len(list1[0])+len(list1[1])); 
traverse.append(len(list1[0])+len(list1[1])+len(list1[2])); 
traverse.append(len(list1[0])+len(list1[1])+len(list1[2])+len(list1[3])); 
traverse.append(len(list1[0])+len(list1[1])+len(list1[2])+len(list1[3])+len(list1[4]));                
          
Timelist=[];
#Timelistf=[];
for i in range(len(list1)):
    for j in range(len(list1[i])):
        #print [{i:list1[i][j]}]
        Timelist.append([{i:list1[i][j]}]);
    #Timelistf.append(Timelist)
print Timelist;

#Temporal communities

TCOMM=Timelist[:];

#print TCOMM; Cross-Verify

count=0;
for i in  range(len(t1list2)-1,-1,-1):
    popp=[];
    for j in range(len(t1list2[i])-1,-1,-1):
        #print i,j;
        if t1list2[i][j]<100:
            #print len(TCOMM)-len(partition5)-1-count, traverse[i]+t1list2[i][j]-1,i,j
            TCOMM[len(TCOMM)-len(partition5)-1-count].extend(TCOMM[traverse[i]+t1list2[i][j]-1]);
            popp.extend([traverse[i]+t1list2[i][j]-1]);
        count=count+1;
        #print i,j,count;
    print popp;
    for k in range(len(popp)):
        TCOMM[popp[k]]='None';
    
    
#removing None values to get final pre-Split-Merge:
    
for i in range(len(TCOMM)):
    if TCOMM[i]=='None':
        TCOMM.pop(i);
for i in range(len(TCOMM)):
    print TCOMM[i];
     
    

import pickle

with open("/home/pk/Python Wd/Python wd_old/split_merge_new1.txt",'wb') as f:
   pickle.dump(TCOMM,f)


