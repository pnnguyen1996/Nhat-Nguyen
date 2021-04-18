#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
#r=2
n=5
q= 79 #next_prime(2^10)
    #def GenTrap(n,q,r):
m_1=20 #int(2*n*log(q,2))
m_2=10
#l= int(log(q,r))
#d=int(2*n*log(q,2))

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
A,T_A=Matrix_Basis(n,m_1,q)

M=matrix(GF(q),np.random.randint(q,size=(n,m_2)))


# In[41]:


print(A_1*S)


# In[45]:


def ExtBasis(A,M,T_A):
    W=matrix(ZZ,A.solve_right(-M))
    T_A1=matrix(ZZ,(T_A.augment(W)).stack(zero_matrix(ZZ,m_2,m_1).augment(identity_matrix(ZZ,m_2))))
    A_1=matrix(GF(q),A.augment(M))
    return A_1, T_A1
A_1,T_A1=ExtBasis(A,M,T_A)


# In[46]:


A_1*T_A1


# In[ ]:




