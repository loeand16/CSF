# Name: Andrew Loewen
# Evergreen Login: loeand16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408

#to solve the plus, indicated by x
x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
#to solve the minus, indicated by y
y = (-b - math.sqrt(b**2 - 4*a*c))/2*a

print x
print "and"
print y


###
### Problem 2
###

print "Problem 2 solution follows:"

from hw1_test import *

letters =[a,b,c,d,e,f]

for index in range(len(letters)):
        print letters[index]



###
### Problem 3
###

print "Problem 3 solution follows:"

print "(("+str(letters[0])+" and "+str(letters[1])+") or (not "+str(letters[2])+") and not ("+str(letters[3])+" or "+str(letters[4])+" or "+str(letters[5])+"))" 


###
### Collaboration: http://www.tutorialspoint.com/python/python_basic_operators.htm, http://repl.it/languages/Python, Matt Schult
