# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:02:33 2019

@author: User
"""
import numpy as np
class tensor:
     def __init__(self,index):
         self.index = index
         noe = np.prod(index)
         self.t = np.zeros(noe).reshape(index)

#------------------------------------partial trace----------------------------------------------------         
     def ptrace(self,i,j):
         if(self.index[i] != self.index[j]):
             print("dimensions dont match!")
         newindex = self.index.copy()
         del newindex[i]
         del newindex[j-1]
         if newindex == []:
             d = sum(self.t[l,l] for l in range(self.index[i]))
             return d
         else :    
            d = tensor(newindex)
            for k,value in np.ndenumerate(d.t):
                m = list(k)
                for l in range(self.index[i]):
                    if l == 0:
                        m.insert(i,l)
                        m.insert(j,l)
                    else:
                        m[i] = l
                        m[j] = l
                    n = tuple(m)   
                    d.t[k] = d.t[k] + self.t[n]
            return d
#---------------------------------contract two indices------------------------------------------------------------------             
     def contract(self,b,index):
         newindex = self.index + b.index
         d = tensor(newindex)
         for j,v in np.ndenumerate(self.t):
             for k,w in np.ndenumerate(b.t):
                 i = list(j+k)
                 m = tuple(i)
                 d.t[m] = (v*w)
         if index == []:
             return d
         else:
             return d.ptrace(index[0],index[1])
         
            
     def contractmultiple(self,b,index):
         newindex = self.index + b.index
         d = tensor(newindex)
         for j,v in np.ndenumerate(self.t):
             for k,w in np.ndenumerate(b.t):
                 i = list(j+k)
                 m = tuple(i)
                 d.t[m] = (v*w)
         if index == []:
             return d
         else:
             for i in index:
              d = d.ptrace(i[0],i[1])
             return d
#-----------------------------delta------------------------------------------------------------------         
class delta(tensor):
    def __init__(self,index):
        tensor.__init__(self,index)
        for i,value in np.ndenumerate( self.t ):
            if len(set(i))==1:
                self.t[i] = 1
    

t1 = delta([2])
t2 = delta([2])
t3 = (t1.contract(t2,[0,1]))



