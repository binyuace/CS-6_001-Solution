# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Problem Set 1
# Name: Bin Yu
# Time: 21/April/2017/ 14:00-16:45
from math import *
import math
odd=3
iterations=2
prime=[2,3]
candidate=[1,3]
i=2
while i<100000:
    i+=1
    candidate.append(2*i-1)
    
def isprime(x):
    y=x/2
    while x%y>0:
        y=y-1 
        if y==1: 
            return 1
print candidate[1000]
        
iterations=2
while iterations<10000:       
    if isprime(candidate[iterations]):
        prime.append(candidate[iterations])
    iterations+=1      
        
print prime[999]

n=input('input n  ')
j=0
product=0
while prime[j]<n:
    j+=1
m=0
while m<j: 
    product+=log(prime[m])
    m+=1
print product/n             


          
    
