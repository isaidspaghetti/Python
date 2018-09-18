#Anagrams
#Check if two strings are anagrams using checking off method
def anagramCheckoff (string1, string2):
    #strings are immutable, string1 does not need to be changed but 2 does. convert to list
    string1 =string1.lower()
    string2 = string2.lower()
    list2=list(string2)

    #check if each item in list1 is in list 2
    #ii is character in string1
    ii=0
    #start by assuming is an anagram
    isAnagram = True
    while ii < len(string1) and isAnagram:
        #jj is character in string2
        jj = 0
        found = False
        while jj < len(list2) and not found:
            if string1[ii] == list2[jj]:
                found = True
            else:
                jj += 1
            # once we find a match remove both from the list. Must include else repeated letters in string1
            # will always be found
        if found:
            list2[jj] = None
        else:
            isAnagram = False
        ii += 1
    return isAnagram

print (anagramCheckoff('racecar','carecar'))
print (anagramCheckoff('raCecar','carecar'))
print (anagramCheckoff('racecar','catecar'))

#anagrams are only anagrams if they are the same when alphabetically sorted
def anagramSort_Compare(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()

    ii=0
    isAnagram = True

    while ii < len(string1) and isAnagram:
        if list1[ii] == list2[ii]:
            ii += 1
        else:
            isAnagram = False
    return isAnagram

print (anagramSort_Compare('racecar','carecar'))
print (anagramSort_Compare('raCecar','carecar'))
print (anagramSort_Compare('racecar','catecar'))

#Countand Compare - if only using alphanumerics we can just count how many times each letter occurs

def count_and_compare(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    #counters
    counter1 = [0] * 26
    counter2 = [0] * 26

    for ii in string1:
        pos = ord(string1[ii])-ord('a')