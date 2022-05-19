#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("play.csv")
data


# In[2]:


import numpy as np


# In[12]:


np.array(data)[0:3]


# In[ ]:





# In[13]:


conc=np.array(data)[:,:-1]
conc


# In[14]:


tar=np.array(data)[0:5,-1:]
tar


# In[10]:


for x in tar:
    print(x)


# In[15]:


def finds(tar,conc):
    for i,val in enumerate(tar):
        if val=='yes':
            spec=conc[i].copy()
            break
    for i,val in enumerate(conc):
        if tar[i]=='yes':
            for x in range(len(spec)):
                if val[x] !=spec[x]:
                    spec[x]="?"
                else:
                    pass
            print("the mainly specific hypothesis is",i)
            print(spec)
print(finds(tar,conc))


# In[16]:


def cand(conc, tar): 
    specific = conc[0].copy()
    
    print("\nSpecific Boundary: ", specific)
    general = [["?" for i in range(len(specific))] for i in range(len(specific))]
    print("\nGeneric Boundary: ",general)  

    
    for i, val in enumerate(conc):
        print("\nInstance", i+1 , "is ", val)

        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    specific[x] ='?'                     
                    general[x][x] ='?'
                
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    general[x][x] = specific[x]                              
                else:                    
                    general[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific)         
        print("Generic Boundary after ", i+1, "Instance is ", general)
        print("\n")

    indices = [i for i, val in enumerate(general) if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        general.remove(['?', '?', '?', '?', '?', '?']) 
    
    return specific, general 
s_final, g_final = cand(conc, tar)

print("Final Specific: ", s_final, sep="\n")

print("Final General: ", g_final, sep="\n")


# In[ ]:




