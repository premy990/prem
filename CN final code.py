# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 14:23:05 2017

@author: prem
"""
import pickle
import numpy as np
import operator

with open("/home/pk/Python Wd/Python wd_old/split_merge.txt",'rb') as f:
#with open("/home/pk/Python Wd/Python wd_old/cn project/split_merge_rework.txt",'rb') as f:
    splinput=pickle.load(f)

##################Running Split-Merge########################

CF=[]
CI=splinput
out = np.empty(4, dtype=object)
#ci of paper =set(cnode)

for ci in CI:
   # AllCnode=[]#All the nodes with repetitions in all communities
    #for commi in range(len(CI)):
        cnode=[]
        for key in range(len(ci)):
            s= ci[key].values()
            flattened = [val for sublist in s for val in sublist]
            #print key,flattened
            cnode.extend(flattened)
        #print cnode
            #AllCnode.append(cnode)
      
        #Final INA Values for unique nodes of all communities
        #INAnode=[]  #unique node in all communities
        #for i in range(len(cnode)):
        INA=[]
        scnode=set(cnode)
        for node in scnode:
                #print i,node,INAnode[i].count(node)
            INA.append(1-1.0/(cnode.count(node)))
        #print INA
        
        # INA means and sd for each community
        INAA=np.asarray(INA)
                
        INAm=np.mean(INAA)
        #print INAm
        INAsd=np.var(INAA)**0.5
        #print INAsd
        #MSD=zip(INAm,INAsd) 
        #print MSD   
        for k in range(1,4):
            out[k]=[]
        
        C=[]
        for nj in scnode.copy():
            INA=1-1.0/(cnode.count(nj))
            #print INA
            delta='TRUE'
            for k in range(3,0,-1):
                if (INA<INAm-k*INAsd and delta=='TRUE'):
                    out[k].append(nj)
                    delta='FALSE'
                    #print k,out,delta,nj
            for k in range(3,0,-1):
                if out[k]!=[]:
                    for i in range(len(ci)):
                        if nj in ci[i].values()[0]:
                            ci[i].values()[0].remove(nj)
                            #print ci
                            C.append({ci[i].keys()[0]:[nj]})
                            #print C
                out[k]=[]
        
        CF.append(ci)
        if C!=[]:
            CF.append(C)
        #print CF
        
############################ Merge ########################################

DELTA='FALSE'
Ni=0
ni=0
while DELTA=='FALSE':
    S=[]
    print S
    for i in range(len(CF)):
        cnodei=[]
        nik=[]
        nik1=[]
        
        for key in range(len(CF[i])):
            s= CF[i][key].values()
            flattened = [val for sublist in s for val in sublist]
            #print key,flattened
            cnodei.extend(flattened)
        scnodei=set(cnodei)
        Ni=len(scnodei)
        ni=len(cnodei)
        #print scnode,N,n
        for node in scnodei:
            nik.append(cnodei.count(node))
            #print node,cnode.count(node),nik
        #print nik,cnode
            
        Nj=0
        nj=0        
        nik=np.asarray(nik)
        
        
        for j in range(len(CF)):
            if (i!=j):
                cnodej=[]
                njk=[]
                njk1=[]
                for key in range(len(CF[j])):
                    s= CF[j][key].values()
                    flattened = [val for sublist in s for val in sublist]
                    #print key,flattened
                    cnodej.extend(flattened)
                scnodej=set(cnodej)
                Nj=len(scnodej)
                nj=len(cnodej)
                
                for node in scnodei:
                    njk.append(cnodej.count(node))
                #print i,j,nik,njk,cnodej
                
                njk=np.asarray(njk)

                if len(njk)<len(nik):
                    nik=nik[0:len(njk)]
                else:
                    njk=njk[0:len(nik)]
                poij=(np.inner(nik,njk))/(Ni*ni*nj*1.0)
               # print poij,np.inner(nik,njk),Ni,ni,nj
                
                

                for node in scnodej:
                    njk1.append(cnodej.count(node))   
                for node in scnodej:
                    nik1.append(cnodei.count(node))                
                
                
                if len(nik1)<len(njk1):
                    njk1=njk1[0:len(nik1)]
                else:
                    nik1=nik1[0:len(njk1)]
                poji=(np.inner(nik1,njk1))/(Nj*ni*nj*1.0)
               # print poji
                
                po=min(poij,poji)
               # print po
            if i<j:
                if po > .005:
                    S.append(CF[i])
                    S.append(CF[j])
                S_new=[]
                for el in S:
                    if el not in S_new:
                        S_new.append(el)
                S=S_new
                    
                    
    CM=CF
    #print S
    if S==[]:
        DELTA='TRUE'
    else:
        NAM=0
        for i in range(len(S)):
            for j in range(len(S)):
                if i<j:
                    #CFcopy=[]
                    #CFcopy.extend(CF)
                    CFcopy=CF[:]
                    Cdash=[]
                    temp=[]
                    print i,j,CF[0]
                    CFcopy.remove(S[i])
                    print 'done1',S[i],S[j]
                    CFcopy.remove(S[j])
                    print 'done2'
                    Cdash.extend(CFcopy)
                    temp.extend(S[i])
                    temp.extend(S[j])
                    Cdash.append(temp)
                    #print S,i,j
                    scnodena=[]
                    
                    #Cdash.remove(None)
                    for i in range(len(Cdash)):
                        cnodena=[]
                        for key in range(len(Cdash[i])):
                            s= Cdash[i][key].values()
                            flattened = [val for sublist in s for val in sublist]
                            #print i,key,flattened
                            cnodena.extend(flattened)
                            scnodena=set(cnodena)
                            #print len(scnodena)
                            NACdash=1-len(scnodena)/(len(cnodena)*1.0)
                            if NACdash>NAM:
                                NAM=NACdash
                                CM=Cdash
                                #print NAM,'in'
    CF=CM
    print DELTA
    
    