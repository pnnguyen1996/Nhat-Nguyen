#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
n= 2^8
def tn(x):
    return log(x,2)
def gaussian(s,c,x):
    return exp((-pi*(x-c)^2)/s^2)
def sampleZalgorithm(s, c, iter):
    samples = []
    l =c -s*tn(n)
    r = c+ s*tn(n)
    for i in range(iter):
        x= random.uniform(l,r)
        accept = random.uniform(0,1)
        if accept < gaussian(s,c,x): 
            samples.append(x)
    return samples
y=sampleZalgorithm(2,0,1000)
histogram(y,density=True)


# In[ ]:





# In[ ]:




