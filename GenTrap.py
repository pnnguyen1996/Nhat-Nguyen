#!/usr/bin/env python
# coding: utf-8


import numpy as np
#m_1>=d = (1+sigma)n logq
#m_2>=l*m_1
r=2
n=10
q= next_prime(2^10)
#def GenTrap(n,q,r):
m_1=int(2*n*log(q,2))
l= int(log(q,r))
d=int(2*n*log(q,2))
m_2=l*m_1
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
HH=(H-C).T
#generate matrix P
P=np.zeros((m_2,m_1),int)
for i in range(m_1):
    for j in range(m_2):
        if j==(i+1)*l-1:
            P[j][i]=1
P=matrix(ZZ,P)

#generate matrix G
G_list=list(np.zeros(m_1,dtype=int))
for i in range(m_1):
    G_list[i]=(np.matrix((HH)[i])/(r**(l-1))).astype(int)
    for j in range(l-1):
        G_list[i]=np.append(G_list[i],(np.matrix((HH)[i])/(r**(l-j-2))).astype(int),axis=0)
    G_list[i]=matrix(G_list[i]).T
G=G_list[0]
for i in range(1,len(G_list)):
        G=np.append(G,G_list[i],1)
G=matrix(ZZ,G)

#generate matrix U
U=np.identity(m_2,int)
for i in range(m_2):
        if i<m_2-1:
            U[i][i+1]=-r
U=matrix(ZZ,U)

#generate matrix R
R=np.zeros((m_1,m_2),int)
for i in range(m_1):
    for j in range(m_2):
        rand1=int((np.random.randint(4,size=1))[0])
        if  rand1==2:
            R[i][j]= 1
        elif rand1== 3:
            R[i][j]=-1
R=matrix(ZZ,R)
A_2=-A_1*(G+R)
A=matrix(np.concatenate((A_1,A_2),axis=1))
S_up=matrix(np.concatenate((((G+R)*U),R*P-C),axis=1))
S_down=matrix(np.concatenate((U,P),axis=1))
S= matrix(np.concatenate((S_up,S_down),axis=0))
    #return list((A,S))
#A=GenTrap(n,q,r)[0]
#S=GenTrap(n,q,r)[1]


# In[20]:


G*P==HH.T


# In[21]:


A*S==matrix(np.zeros((n,m_1+m_2),int))


# In[22]:


X=(A.rows())[1]
for i in range(n-1):
    X=np.concatenate((X,(A.rows())[i+1]))
histogram(X)


# In[23]:


A_1*H==matrix(np.zeros((10,200),int))


# In[24]:


matrix(GF(q),A*S)==matrix(np.zeros((10,2200),int))


# In[ ]:


A_1=matrix(GF(q),np.random.randint(7,size=(10,4)))
def q_arybasis(A_1,q):
    n=len(A_1.rows())
    m=len(A_1.columns())
    H=matrix(ZZ,(((A_1)).kernel()).basis())
    O=zero_matrix(ZZ,m,n-m)
    qI= q*identity_matrix(ZZ,m)
    K=O.augment(qI)
    M=H.stack(K)
    return M
L=q_arybasis(A_1,7)
print(L)
H=matrix(ZZ,(((A_1).T).kernel()).basis()).T
print()
print(H)
L*A_1

