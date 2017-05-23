# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:21:40-23:07 problem 1-3
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    subdic={}
    for line in inputFile:
        splitline=line.split(',')
        subdic[splitline[0]]=(int(splitline[1]),int(splitline[2].strip()))
    return subdic
            

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).
subdic=loadSubjects(SUBJECT_FILENAME)

    
def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#  greedyAdvisor(subdic, 20,cmpValue)
def greedyAdvisor(subjects, maxwork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
   
    
    subcopy=subjects.copy()
    final={}
    while maxwork > 0:
        templist=[0,1000]
        temp=''
        for items in subcopy:
            subinfo1=subcopy[items]
            if comparator(subinfo1,templist) and subinfo1[1]<=maxwork:
                templist = subinfo1
                temp=items
        if temp!='':
            final[temp]=templist
            #print temp, templist
            maxwork=maxwork-templist[1]
            del subcopy[temp]
        else: break
    return final



def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(subjects,maxWork):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    start= time.time()
    
    bruteForceAdvisor(subjects, maxWork)
    end= time.time()
    totaltime=end-start
    print totaltime
    return totaltime



# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#

def total_value(sublist,subjects):
    y=0
    for x in sublist:
#        if type(x) is str:
#            print x, 'fuck'
#            return 0
        assert type(x) is str
        
        y = y + subjects[x][0]
    return y
            
    
memory = {}

def dPAdvisor(subjects, maxWork,name):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work) 
    """
    assert type(subjects) is dict
    assert type(memory) is dict
    try: return memory[(name,maxWork)]
    except KeyError:
        if len(name)==0:
            memory[(name,maxWork)]=()
            return ()
        if maxWork<=0:
            memory[(name,maxWork)]=()
            return ()
        last=subjects[name[-1]]
        lastwork=last[1]
        lastvalue=last[0]
        if len(name) == 1: 
            if maxWork>= lastwork:
                memory[(name,maxWork)] = (name[-1],)
            else: memory[(name,maxWork)] = ()

        newname=name[:-1]
        assert type(memory) is dict
        if lastwork > maxWork:
            memory[(name,maxWork)]=dPAdvisor(subjects, maxWork,newname)
            assert type(memory) is dict
        else:
            if total_value(dPAdvisor(subjects, maxWork,newname),subjects) > lastvalue + total_value(dPAdvisor(subjects, maxWork-lastwork,newname),subjects):
                memory[(name,maxWork)] = dPAdvisor(subjects, maxWork,newname)
                assert type(memory) is dict
            else:
                memory[(name,maxWork)] = (name[-1],) + dPAdvisor(subjects, maxWork-lastwork,newname)
                assert type(memory) is dict
    assert type(memory) is dict                  
    return memory[(name,maxWork)]
def dpAdvisor(subjects, maxWork):
    assert type(subjects) is dict
    final={}
    name=[]
    for items in subjects:
        name.append(items)
    name = tuple(name)
    subtuple = dPAdvisor(subjects, maxWork,name)
    print subtuple
    print 'p'
    for items in subtuple:
        final[items]=subjects[items]
    return final
        
            
                        
            
            
        
        
    
    
    
print

finalanswer = dpAdvisor(subdic,10) 
  
printSubjects(finalanswer)   
#greedy=greedyAdvisor(subdic, 7, cmpValue)    
#brute=bruteForceAdvisor(subdic,10) 
#printSubjects(brute)   
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime(subjects,maxWork):
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    start=time.time()
    printSubjects(dpAdvisor(subjects, maxWork))    
    end = time.time()
    return end -start
    
    # TODO...
print dpTime(subdic,100)
# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
