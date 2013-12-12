# Name: Andrew Loewen
# Evergreen Login: loeand16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

a = 2
b = 2

#assert a == b

#After changing the assignment of b to 3, the syntax is still invalid

#The interpreter gives no messages when a and b both equal 2, but when b equals 3, the interpreter says:

#"Traceback (most recent call last):
#File "<input>", line 1, in <module>
#AssertionError

#The assert statement is evaluating the boolean value of the argument, and returns an error if the value is false

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

def add(a,b):
	return a + b

total = add(a,b)
print total

print "Functions are defined by the suffix 'def' followed by a name and a designated input variable, and end with 'return'"

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

v = {"a":2, "b":3}
assert v == {"a":2, "b":3}

print "A dictionary is unordered and immutable."

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

v2={}
v2["a"]=a
v2["b"]=b

assert v==v2

# This method allows the programmer to add key pairs without having to retype the whole dictionary

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

for k in v:
	print k

for k in v:
	print k
	print v[k]

# The command to print k prints the key whereas the command to print v[k] prints the value assigned to each key

###
### Collaboration
###

# Brandon Anderson
