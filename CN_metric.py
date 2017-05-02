# NA
Na=[]
for i in range(len(CF)):
   cnodena=[]
   for key in range(len(CF[i])):
       s= CF[i][key].values()
       flattened = [val for sublist in s for val in sublist]
       #print i,key,flattened
       cnodena.extend(flattened)
       scnodena=set(cnodena)
       #print len(scnodena)
       NAC=1-len(scnodena)/(len(cnodena)*1.0)
       Na.extend([NAC])
np.mean(Na)        

with open("/home/pk/Desktop/CN project/split_merge_real2.txt",'rb') as f:
#with open("/home/pk/Python Wd/Python wd_old/cn project/split_merge_rework.txt",'rb') as f:
    splinput=pickle.load(f)
    

Na=[]
for i in range(len(splinput)):
   cnodena=[]
   for key in range(len(splinput[i])):
       s= splinput[i][key].values()
       flattened = [val for sublist in s for val in sublist]
       #print i,key,flattened
       cnodena.extend(flattened)
       scnodena=set(cnodena)
       #print len(scnodena)
       NAC=1-len(scnodena)/(len(cnodena)*1.0)
       Na.extend([NAC])
np.mean(Na)        
