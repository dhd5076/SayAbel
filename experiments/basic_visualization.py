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
        neurons_per_layer = 12
        for i in range(0,144):
            self.neurons.append({
                'X': 200 + (64 * (i // neurons_per_layer)),
                'Y': 400 + (-32 * (i % neurons_per_layer)),
                'LAYER': (i // neurons_per_layer),
                'POSITION': (i % neurons_per_layer),
                'VALUE': 0,
                'CONNECTIONS': []
            })
        for neuron in self.neurons:
            for i in range(len(self.neurons)):
                if neuron['LAYER'] == self.neurons[i]['LAYER'] + 1:
                    neuron['CONNECTIONS'].append([i, random.uniform(-1,1)])
        #create observance
        self.neurons.append({})


def draw_square(x,y,value):
    glColor3f(1 - value, 0, value)

    glVertex2i(x, y)
    glVertex2i(x + 10, y)

    glVertex2i(x + 10, y)
    glVertex2i(x + 10, y + 10)

    glVertex2i(x + 10, y + 10)
    glVertex2i(x, y + 10)

    glVertex2i(x, y + 10)
    glVertex2i(x, y)


def tan_h(x):
    return tanh(x)

def sig(x):
    return 1 / (1 + exp(-x))

def draw_line(x1, y1, x2, y2, value):
    glColor3f(value, 1 - (value - 1), 0)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)


net = NeuralNet()
window_instance = pyglet.window.Window(1024, 786)
fps_display = pyglet.clock.ClockDisplay(format='%(fps).2f fps')

@window_instance.event
def on_key_press(symbol, modifiers):
    pass #on_draw()


time = 0


@window_instance.event
def on_draw():
    delta_time = 0
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

        if(len(neuron['CONNECTIONS'])):
            neuron['VALUE'] = tan_h(neuron['VALUE'])
    glEnd()
    glBegin(GL_QUADS)
    for neuron in net.neurons:
        draw_square(neuron['X'], neuron['Y'], neuron['VALUE'])
    glEnd()
    net.neurons[0]['VALUE'] = sin(time)


def up(dt):
    global time
    time += 0.1


pyglet.clock.schedule_interval(up, 1.0/128.0)
pyglet.clock.set_fps_limit(128)
pyglet.app.run()
