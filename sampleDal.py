#!/usr/bin/env python
# coding: utf-8

# In[88]:


import random
n= next_prime(2^10)
q= 8
m=50
def tn(x):
    return log(x,2)
def gaussian(s,c,x):
    return exp((-pi*(x-c)^2)/s^2)
#SampleZ Al. here
def sampleZalgorithm(s, c, iter):
    l = int(c -s*tn(n))
    r = int(c+ s*tn(n))
    for i in range(iter):
        x= random.randint(l,r)
        accept = random.uniform(0,1)
        if accept < gaussian(s,c,x): 
            samples = x
            break
    return samples
#generate an arbitrary lattice with demension m*m
def independent_vector(m):
    B=(matrix(ZZ,np.random.randint(q,size=(m,1)))) #first vector of B
    size_B=1
    B_1=[vector(B)]
    while size_B < m:
        A = (matrix(ZZ,np.random.randint(q,size=(m,1))))
        if B.rank()==m:
            break
        h=(B.T).rank()
        if ((B.augment(A)).T).rank()==h+1:
            B=B.augment(A) 
            size_B=size_B+1
            B_1=B_1+[vector(A)]
    return(B_1)
#old code
#B = [vector([1,2,5]), vector([1,2,3]), vector([-1,0,0])]
#from sage.modules.misc import gram_schmidt
#G, mu = gram_schmidt(B)
#G
#s=50
c=zero_vector(ZZ,m)
v=zero_vector(ZZ,m)
B=independent_vector(m) #B is a list of m independent vectors
from sage.modules.misc import gram_schmidt
G, mu = gram_schmidt(B)
s=50
def sampleDalgorithm(iter):
    samples=[]
    Bc = list(zero_vector(ZZ,m))+[c]
    Bv = list(zero_vector(ZZ,m))+[v]
    for j in range(iter):
        for i in range(m,0,-1):
            ci = Bc[i].dot_product(G[i-1])/(G[i-1].dot_product(G[i-1]))
            si= s/((G[i-1].dot_product(G[i-1]))^(1/2))
            zi= sampleZalgorithm(si,ci,n)
            Bc[i-1]=Bc[i]-zi*B[i-1]
            Bv[i-1] = Bv[i] +zi*B[i-1]
        samples.append(Bv[0])
    return(samples)
histogram(sampleDalgorithm(200))


# In[78]:


B = matrix([[1,2,5], [1,2,3], [-1,0,0]])
B_1=list(B[0])
B_1[1]


# In[80]:


B=(matrix(ZZ,np.random.randint(q,size=(3,1)))) #first vector of B
size_B=1
B_1=[vector(B)]
while size_B < m:
    A = (matrix(ZZ,np.random.randint(q,size=(m,1))))
    if B.rank()==m:
        break
    h=(B.T).rank()
    if ((B.augment(A)).T).rank()==h+1:
        B=B.augment(A) 
        size_B=size_B+1
        B_1=B_1+[vector(A)]


# In[81]:


B_1


# In[ ]:




