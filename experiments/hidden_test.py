
"""
My first proper implementation of a neural network with hidden layers
"""
from numpy import *


def sig(x):
    return 1 / (1 + exp(-x))


test_data = array([[0,0,
                    1,1],

                   [1,0,
                    0,1],

                   [1,0,
                    1,0]])

expected_output = array([[1,0,0,0],
                         [0,0,1,0],
                         [0,1,0,0]])

depth = 20
out = test_data[0]
weights = random.random_integers(-1,1,(len(out),len(out), depth)).T
for i in range(0, len(weights)):
    out = sig(dot(out, weights[i]))

print("Horizontal", out[0])
print("Vertical",   out[1])
print("Diagonal",   out[2])
print("Other",      out[3])
