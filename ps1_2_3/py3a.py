from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def countSubStringMatch(target,key):
    j=0
    
    for i in range (len(target)-len(key)+1):
      last=last= i+len(key)
      if key==target[i:last]:
          j+=1
  
    if j==target.count(key):
      return j
    else:
        return 'none'
        
    


    
        
    
    
    
def countSubStringMatchRecursive (target, key):
    last=len(key)
    if last>len(target):
        return 0
    if key==target[0:last]:
        target=target[1:]
        return 1+countSubStringMatchRecursive(target,key)
    else:
        target=target[1:]
        return countSubStringMatchRecursive(target,key)
        
        
        
print countSubStringMatch(target1,key10)

print countSubStringMatchRecursive(target1,key10)

def subStringMatchExact(target,key):
    list=()
    for i in range (len(target)-len(key)+1):
      last=last= i+len(key)
      if key==target[i:last]:
          list+=(i,)
          
    return list



def constrainedMatchPair(firstMatch,secondMatch,length):
    list=()
    for n in range(len(firstMatch)):
        for m in range(len(secondMatch)):
            if firstMatch[n]+length+1==secondMatch[m]:
               list+=(firstMatch[n],) 


    return list





def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers


def subStringMatchExactlyOneSub(target,key):
    alllist=subStringMatchOneSub(target,key)
    exactlist=subStringMatchExact(target,key)
   

print subStringMatchOneSub(target1,key11)       


  
print subStringMatchExact(target1,key11)  
print subStringMatchExactlyOneSub(target1,key13)























     




   
