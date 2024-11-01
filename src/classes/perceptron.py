import numpy as np


class Perceptron:
    def __init__(self, inputs, outputs, learning_rate):
        self.inputs = inputs
        self.outputs = outputs
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(0, 1, 4)
        self.epochs = 0

    def bipolarStepActivationFunction(self, u):
        if u >= 0:
            return 1
        return -1

    def training(self):
        error = 1

        while error != 0:
            error = 0
            self.epochs += 1

            for i in range(len(self.inputs)):
                x = np.array(self.inputs[i])

                u = np.dot(x, self.weights)

                y = self.bipolarStepActivationFunction(u)

                error = self.outputs[i] - y

                if y != self.outputs[i]:
                    self.weights += self.learning_rate * error * x

    def operation(self, inputs):
        u = np.dot(inputs, self.weights)
        return self.bipolarStepActivationFunction(u)
