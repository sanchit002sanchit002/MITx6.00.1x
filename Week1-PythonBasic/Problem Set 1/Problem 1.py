"""
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
"""

#test-code
#s = 'azcbobobegghakl'

def problem1(s):
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    print ("Number of vowels:",count)

problem1(s)
