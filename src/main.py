import numpy as np


class Perceptron:
    def __init__(self):
        self.weights = np.random.uniform(0, 1, 4)
        self.epochs = 0

        print(
            f"Pesos iniciais:\nw0: {self.weights[1]:.4f}\nw1: {self.weights[2]:.4f}\nw2: {self.weights[3]:.4f}"
        )
        print(f"Bias inicial: {self.weights[0]:.4f}\n")

    def bipolarStepActivationFunction(self, u):
        if u >= 0:
            return 1
        return -1

    def training(self, inputs, outputs, learning_rate):
        error = 1

        while error != 0:
            error = 0
            self.epochs += 1

            for i in range(len(inputs)):
                x = np.array(inputs[i])

                u = np.dot(x, self.weights)

                y = self.bipolarStepActivationFunction(u)

                error = outputs[i] - y

                if y != outputs[i]:
                    self.weights += learning_rate * error * x

    def operation(self, inputs):
        u = np.dot(inputs, self.weights)
        return self.bipolarStepActivationFunction(u)


inputs = []
outputs = []
samples = [
    [-1, -0.356, 0.0620, 5.9891],
    [-1, -0.7842, 1.1267, 5.5912],
    [-1, 0.3012, 0.5611, 5.8234],
    [-1, 0.7757, 1.0648, 8.0677],
    [-1, 0.1570, 0.8028, 6.3040],
    [-1, -0.7014, 1.0316, 3.6005],
    [-1, 0.3748, 0.1536, 6.1537],
    [-1, -0.6920, 0.9404, 4.4058],
    [-1, -1.3970, 0.7141, 4.9263],
    [-1, -1.8842, -0.2805, 1.2548],
]


with open("training.txt", "r") as file:
    for line in file:
        values = line.split()

        data = [float(value) for value in values[:4]]

        inputs.append(data)
        outputs.append(float(values[4]))

inputTest = []
outputTest = []


with open("test.txt", "r") as file:
    for line in file:
        values = line.split()

        data = [float(value) for value in values[:4]]

        inputTest.append(data)

        outputTest.append(float(values[4]))


def trainModel(learning_rate):
    model = Perceptron()
    model.training(inputs, outputs, learning_rate)

    print(f"Quantidade de épocas: {model.epochs}\n")
    print(
        f"Pesos finais:\nw0: {model.weights[1]:.4f}\nw1: {model.weights[2]:.4f}\nw2: {model.weights[3]:.4f}"
    )
    print(f"Bias final: {model.weights[0]:.4f}\n")

    print("Base de testes:\n")
    for i in range(0, len(inputTest)):
        y = model.operation(inputTest[i])
        if y == -1:
            print(f"""Resultado esperado: {outputTest[i]}  |   Saída: {y}""")
        else:
            print(f"""Resultado esperado: {outputTest[i]}   |   Saída: {y}""")

    print("\nAmostras:\n")

    for i in range(0, len(samples)):
        y = model.operation(samples[i])
        print(f"Amostra {i+1} = {y}")


def countModelTraining(c):
    print(
        f"""\n--------------------------------------------------
|                    Modelo {c}                    |
--------------------------------------------------\n"""
    )


for i in range(5):
    countModelTraining(i + 1)
    trainModel(0.01)
