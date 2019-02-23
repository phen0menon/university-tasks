import numpy as np
from numpy import dot

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def append_vector(vector):
    return np.concatenate((vector, [[1]]), axis=1)

class Layer:
    def __init__(self, number_of_inputs_neuron, number_of_neurons):
        self.weights = 2 * np.random.random((number_of_neurons, number_of_inputs_neuron)) - 1

    def get_weights(self):
        return self.weights


class Network:
    current_vector = None

    def __init__(self, layers):
        self.layers = layers

    def set_input(self, inputs):
        self.inputs = inputs
        self.current_vector = inputs

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
            next_vector = sigmoid(dot(self.current_vector, layer.get_weights()))

            if (index != len(self.layers) - 1):
                next_vector = append_vector(next_vector)

            self.current_vector = next_vector
            print(next_vector)


def generate_vector(length):
    return append_vector(2 * np.random.random((1, length)) - 1)

if __name__ == "__main__":
    first_neuron_length = 4

    n_net = Network(np.array([Layer(first_neuron_length, 5), Layer(3, 5), Layer(2, 4)]))
    n_net.set_input(generate_vector(first_neuron_length))

    print("Original Network:")
    n_net.print_layers()

    print("Original Inputs:")
    print(n_net.get_input(), "\n")

    print("Result:")
    n_net.set_dotted()