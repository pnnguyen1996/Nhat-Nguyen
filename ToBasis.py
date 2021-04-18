#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
#r=2
n=5
q= 79 #next_prime(2^10)
    #def GenTrap(n,q,r):
m_1=20 #int(2*n*log(q,2))
#l= int(log(q,r))
#d=int(2*n*log(q,2))
def Euclide_length(A):
    length = 0
    x=len(A)
    for i in range(x):
        length=length+A[i]*A[i]
    length = sqrt(length)
    return length
    
    #generate lattice and it's basis
def Matrix_Basis(n,m_1,q):
    #m_2=l*m_1
    A_1=matrix(GF(q),np.random.randint(q,size=(n,m_1)))
    C=matrix(ZZ,np.identity(m_1, dtype= int))
    
    #hermite normal form basis function.
    def q_arybasis(A_1,q):
        H=matrix(ZZ,((A_1).right_kernel()).basis())
        for i in range(n):
            H= matrix(ZZ,np.concatenate((H,matrix(q*matrix(np.identity(m_1,dtype=int))[m_1-n+i])), axis= 0))
        H=H.T
        return H
    H=q_arybasis(A_1,q)
    return(A_1,H)
A_1,S=Matrix_Basis(n,m_1,q)

#generate linearly independent vectors
def independent_vector(m_1,S):
    B=matrix(S*vector(matrix(ZZ,np.random.randint(q,size=(m_1,1))))).T
    for i in range(1,2*m_1):
        A = vector(matrix(ZZ,np.random.randint(q,size=(m_1,1))))
        A =matrix(S*A).T
        if B.rank()==m_1:
            break
        h=(B.T).rank()
        if ((B.augment(A)).T).rank()==h+1:
            B=B.augment(A) 
    return(B)
V=independent_vector(m_1,S)
Q=matrix(ZZ,(S**(-1))*V)
T = Q.echelon_form()
U= Q*(T**(-1))
S_1=matrix(ZZ,S*U)
print(S_1)


# In[47]:


#Check if S is basis of labda_perp(A_1)
A_1*S


# In[46]:


#check if U is unimodular matrix
U.det()


# In[ ]:




