from numpy import *
import pyglet
from pyglet.gl import *
import collections
from pyglet.window import key

LAYER = 0
POSITION = 1
VALUE = 2
X_POS = 3
Y_POS = 4


class Neuron:

    def __init__(self):
        self.connections = []
        self.connections.append([0,0])


class NeuralNet:

    def __init__(self):
        self.neurons = []
        neurons_per_layer = 6
        for i in range(0,72):
            self.neurons.append({
                'X': 250 + (50 * (i // neurons_per_layer)),
                'Y': 300 + (-50 * (i % neurons_per_layer)),
                'LAYER': (i // neurons_per_layer),
                'POSITION': (i % neurons_per_layer),
                'VALUE': 0,
                'CONNECTIONS': []
            })
        for neuron in self.neurons:
            for i in range(len(self.neurons)):
                if neuron['LAYER'] == self.neurons[i]['LAYER'] + 1:
                    neuron['CONNECTIONS'].append([i, random.random()])
        #self.neurons[0]['VALUE'] = 0


def draw_square(x,y,value):
    glColor3f(0, 0, value)

    glVertex2i(x, y)
    glVertex2i(x + 10, y)

    glVertex2i(x + 10, y)
    glVertex2i(x + 10, y + 10)

    glVertex2i(x + 10, y + 10)
    glVertex2i(x, y + 10)

    glVertex2i(x, y + 10)
    glVertex2i(x, y)


def sig(x):
    return 1 / (1 + exp(-x))

def draw_line(x1, y1, x2, y2, value):
    glColor3f(value / 2, value / 2, 0)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)


net = NeuralNet()
window_instance = pyglet.window.Window(1024, 786)
fps_display = pyglet.clock.ClockDisplay(format='%(fps).2f fps')

@window_instance.event
def on_key_press(symbol, modifiers):
    pass #on_draw()

@window_instance.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    for neuron in net.neurons:
        if len(neuron['CONNECTIONS']) > 0:
            neuron['VALUE'] = 0
        for conn_idx in neuron['CONNECTIONS']:
            draw_line(neuron['X'] + 5,
                      neuron['Y'] + 5, net.neurons[conn_idx[0]]['X'] + 5,
                      net.neurons[conn_idx[0]]['Y'] + 5,
                      conn_idx[1])
            neuron['VALUE'] += (conn_idx[1] * net.neurons[conn_idx[0]]['VALUE'])

        neuron['VALUE'] = sig(neuron['VALUE']) - 0.45
    glEnd()
    glBegin(GL_QUADS)
    for neuron in net.neurons:
        draw_square(neuron['X'], neuron['Y'], neuron['VALUE'])
    glEnd()
    net.neurons[0]['VALUE'] = 1
    #print(net.neurons[0]['VALUE'])


#pyglet.clock.schedule(on_draw)

def up(dt):
    pass

pyglet.clock.schedule_interval(up, 1.0/128.0)
pyglet.clock.set_fps_limit(128)
pyglet.app.run()
