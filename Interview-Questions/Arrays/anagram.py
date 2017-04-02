"""
Problem 1: Anagram Check
Given two strings, check to see if they are anagrams.
Two strings are considered as anagrams if they can be written using
the exact same letters (so you can just rearrange the
letters to get a different phrase or word).

For example:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization.
So "d go" is an anagram of "God" and "dog" and "o d g".

"""

def anagram(str1, str2):
    #make every letter of both strings as lowercase
    str1 = str1.lower()
    str2 =  str2.lower()
    d = {}

    #traversing through the first string and populating the dictionary
    for s in str1:
        count = 1
        if s == " ":
            continue
        if s in d:
            d[s] += 1
        else:
            d[s] = count

    #Now for every string in str2,
    #we will decrease the value of same string in the dictionary
    #So if the given two strings are equal then by the end,
    #the value of every string in dictionary must be zero.
    for s in str2:
        if s == " ":
            continue
        if s in d:
            d[s] -= 1
        else:
            return "The given strings are not Anagrams"

    #Checking the value of every string is zero or not.
    for k in d:
        if d[k] != 0:
            return "The given strings are not Anagrams"
    return "The given strings are Anagrams"

print(anagram("public relation", "crap built on lies"))
