# Name: Andrew Loewen
# Evergreen Login: loeand16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# 

import hw2_test

total = 0
count = 1
while count <= hw2_test.n:
	total = total + count
	count = count + 1
print total




###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for y in range (2,11):
	print (1/float(y))


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(1, n + 1):
	triangular = triangular + i

print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via forumula:", n*(n+1)/2
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
fact = 1

for f in range(n):
    fact = (f+1) * fact
    
print fact


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10

for s in range(numlines):
    p = numlines - s
    factorial2 = 1
    for q in range(p):
        factorial2 = (q+1) * factorial2
    print factorial2


###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
sumofrec = 1

for s in range(numlines):
    p = numlines - s
    factorial2 = 1
    for q in range(p):
        factorial2 = (q+1) * factorial2
    factorial2 = 1.0 / factorial2
    sumofrec = factorial2 + sumofrec
print sumofrec

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# https://wiki.python.org/moin/ForLoop, http://learntofish.wordpress.com/2011/11/11/basic-algorithm-2-sum-of-integers/
#Matt Schult/Alexei McConville/Keir Allison-Bourne
