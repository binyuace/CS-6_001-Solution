#!/usr/bin/env python2
# -*- coding: utf-8 -*-

 # Problem Set 2 (Part I)
 # Name: Bin Yu
 # Collaborators: mac
 # Time: 17:56 24/Apr-20:25
 #
pack=(6,9,20)
x=[0,0,0]
def ans(y,m):
    a=6*y[0]+9*y[1]+20*y[2]
    if a==m:
        return 1
z=0
#list2=[]  
#def plus(bug):
#    return bug+1
#for what in range(20):
#    list.append(what)
#print list    
         
                
def main(n):
        j=0
        while j*pack[0]<=n:
            x[0]=j
            if ans(x,n)==1: 
                #print x 
                return x
            else:
                h=0
                while j*pack[0]+h*pack[1]<=n:
                    x[1]=h
                    if ans(x,n)==1: 
                        #print x 
                        return x
                    else:
                      l=0
                      while j*pack[0]+h*pack[1]+l*pack[2]<=n:
                          x[2]=l
                          if ans(x,n)==1: 
                              #print x 
                              return x
                          else :l+=1
                    h+=1
            j+=1
        return 0 
x2=0
for x1 in range(0,200):
     if main(x1)!=0:
        x2+=1
        if x2==6:
            print main(x1-5)
            x3=x1-5
            break
     
     else:x2=0
print 'Largest number of McNuggets that cannot be bought in exact quantity:'
print x3



              