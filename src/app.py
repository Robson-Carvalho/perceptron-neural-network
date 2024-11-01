import numpy as np
import matplotlib.pyplot as plt
from classes.perceptron import Perceptron
from utils.readFile import *

trainingInputData = getInputData()
trainingOutputData = getOutputData()
testInputData = getTestInputData()
testOutputData = getTestOutputData()
samplesData = getSamplesData()

model = Perceptron(trainingInputData, trainingOutputData, 0.001)
model.training()

print(f"Vetor de pesos finais: {model.weights[1:]}\nBias: {model.weights[0]}")

inputs = np.array(trainingInputData)
outputs = np.array(trainingOutputData)

X, Y, Z = [], [], []

for e, i in enumerate(inputs):
    X.append(i[1] * outputs[e])
    Y.append(i[2] * outputs[e])
    Z.append(i[3] * outputs[e])

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
outputs = np.array(outputs)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


for output in set(outputs):
    text = "C1" if output == -1 else "C2"
    ax.scatter(
        X[outputs == output],
        Y[outputs == output],
        Z[outputs == output],
        label=f"Óleo {text}",
        color="green" if output == 1 else "red",
    )


x, y = np.meshgrid(np.linspace(min(X), max(X), 10), np.linspace(min(Y), max(Y), 10))

# Isolando z da Equação Geral do Plano
z = (-model.weights[1] * x - model.weights[2] * y - model.weights[0]) / model.weights[2]

ax.plot_surface(x, y, z, alpha=0.5, color="black")

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")
ax.set_title(
    f"Equação Geral do Plano:  ({model.weights[1]:.2f})x + ({model.weights[2]:.2f})y + ({model.weights[3]:.2f})z + ({model.weights[0]:.2f}) = 0"
)
ax.legend()
plt.show()
