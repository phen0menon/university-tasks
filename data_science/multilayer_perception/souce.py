import numpy as np
from numpy import dot

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Layer:
    def __init__(self, number_of_inputs_neuron, number_of_neurons):
        self.weights = 2 * np.random.random((number_of_neurons, number_of_inputs_neuron)) - 1
        self.weights = np.concatenate((self.weights, [[1.] * number_of_inputs_neuron]), axis=0)

    def get_weights(self):
        return self.weights

    def set_weights(self, new_weight):
        self.weights = new_weight


class Network:
    def __init__(self, layers):
        self.layers = layers

    def set_input(self, inputs):
        self.inputs = inputs

    def get_input(self):
        return self.inputs

    def get_layers(self):
        return self.layers

    def print_layers(self):
        for index, layer in enumerate(self.layers, start=1):
            print("Layer {}".format(index))
            print(layer.get_weights(), "\n")

    def set_dotted(self):
        for index, layer in enumerate(self.layers):
            if index == 0:
                layer.set_weights(sigmoid(dot(self.inputs, layer.get_weights())))
            else:
                layer.set_weights(sigmoid(dot(self.layers[index - 1].get_weights(), layer.get_weights())))


def generate_vector(length):
    return 2 * np.random.random((1, length)) - 1

if __name__ == "__main__":
    first_neuron_length = 4

    n_net = Network(np.array([Layer(first_neuron_length, 3), Layer(2, 3), Layer(1, 1)]))
    n_net.set_input(generate_vector(first_neuron_length))

    print("Original Network:")
    n_net.print_layers()

    print("Original Inputs:")
    print(n_net.get_input(), "\n")

    print("Dotted layers:")
    n_net.set_dotted()
    n_net.print_layers()