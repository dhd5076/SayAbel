from numpy import *

def sig(x):
    return 1 / (1 + exp(-x))

inp = array([[1,0,0],
             [0,1,0],
             [0,0,1]])

out = array([[1,0,0]])
"""
out = [[1,1,1],
       [1,1,1],
       [1,1,1]]
"""
wht = array([[1,0,0],
             [0,1,0],
             [0,0,1]])

print ":::::::INPUT\n"

def prc(i, w):
    print i
    print "::WEIGHT\n"
    print w
    print "::OUTPUT\n"
    print sig(dot(i,w))

#print out
prc(inp, wht)
print prc([0,1;o,1], wht)