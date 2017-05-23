#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:34:49 2017

@author: king
"""

#Retirement fund
#End of year 1
#F[0] = salary * save * 0.01
#End of year 2
#F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
#End of year 3
#F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    fund=0
    listfund=[]
    for year in range(years):
        fund=salary * save * 0.01+fund*(1+0.01*growthRate)
        listfund.append(fund)
        
    return listfund

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
   
    fund=0
    listfund=[]
    for year in range(len(growthRates)):
        fund=salary * save * 0.01+fund*(1+0.01*growthRates[year])
        listfund.append(fund)
        
    return listfund

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
   
    # TODO: Your code here.
    listfund=[]
    for year in range(len(growthRates)):
        savings=savings*(1+0.01*growthRates[year])-expenses
        listfund.append(savings)
        
    return listfund

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    savs=nestEggVariable(salary, save, preRetireGrowthRates)
    sav=savs[-1]
    low=0
    high=sav+epsilon
    expenses=(low+high)/2
    count=0
    while count<200:
        list=postRetirement(sav, postRetireGrowthRates, expenses)
        if list[-1]>epsilon:
            low=expenses
        elif list[-1]<-epsilon:
            high=expenses
        else: return expenses
        expenses=(low+high)/2
        count+=1
        
    
    
    

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.



