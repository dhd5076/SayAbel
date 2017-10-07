from matplotlib import pyplot as plt
import matplotlib.animation as anim
import random
import math
from numpy import *


def sig(x):
    return 1 / (1 + exp(-x))

def d_dx_sig(x):
    return x * (1-x)

def error(target_plot, test_plot):
    total_error = []
    for x in range(0, len(target_plot),1):
        total_error.append(abs(target_plot[x] - test_plot[x]))
    return total_error

#random.seed(0)

N = 3
input = array([[0,0,1],[0,1,1],[1,0,1],[1,1,0]])
print input
input = random.rand(N,3)
print input
targt = array([random.rand(N,)]).T

weigt = 2 * random.random((3, 1)) - 1

plt.xlabel('Input')
plt.ylabel('Output')
plt.title("Neural Network Training Example")


def think(inputs):
    return sig(dot(input, weigt))

plt.ion()
i = 0
while sum(error(targt,think(input))) > .25:
    plt.clf()
    output = think(input)
    err = targt - output
    adjustment = dot(input.T, err * d_dx_sig(output))

    old_error = sum(error(targt,think(input)))
    old_weight = weigt
    weigt[random.randint(-1,len(weigt))] += random.uniform(-0.01,0.01)
    #weigt = 2 * random.random((3, 1)) - 1
    new_error = sum(error(targt,think(input)))
    if new_error > old_error:
        weigt = old_weight
    i += 1
    if i % 1000 == 0:
        plt.plot(targt, label='target')
        plt.plot(think(input), label='output')
        plt.plot(error(targt, think(input)), label='error')
        plt.legend()
        plt.pause(0.005)

plt.show(0.005)
print weigt


