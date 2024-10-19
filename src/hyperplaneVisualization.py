import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self):
        self.weights = np.random.uniform(0, 1, 4)
        self.epochs = 0

        print(f"Pesos iniciais:\nw0: {self.weights[1]:.2f}\nw1: {self.weights[2]:.2f}\nw2: {self.weights[3]:.2f}")
        print(f"Bias inicial: {self.weights[0]:.2f}\n")

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
                    self.weights += (learning_rate * error * x)

    def operation(self, inputs):
        u = (np.dot(inputs, self.weights))
        return self.bipolarStepActivationFunction(u)

inputs = []
outputs = []  

with open('training.txt', 'r') as file:
    for line in file:
        values = line.split()
        data = [float(value) for value in values[:4]]  
        inputs.append(data)
        outputs.append(float(values[4]))

inputTest = []
outputTest = []  

with open('test.txt', 'r') as file:
    for line in file:
        values = line.split()
        data = [float(value) for value in values[:4]]  
        inputTest.append(data)  
        outputTest.append(float(values[4]))

X = []
Y = []
Z = []

e = 0
for  i in inputs:
    X.append(i[1]*outputs[e])
    Y.append(i[2]*outputs[e])
    Z.append(i[3]*outputs[e])
    e += 1

def trainModel(learning_rate):
    model = Perceptron()
    model.training(inputs, outputs, learning_rate)
    
    print(f"Quantidade de épocas: {model.epochs}\n")
    print(f"Pesos finais:\nw0: {model.weights[1]}\nw1: {model.weights[2]}\nw2: {model.weights[3]}")
    print(f"Bias final: {model.weights[0]}\n")


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for output in set(outputs):
        text = "C1" if output == -1 else "C2"
        ax.scatter(np.array(X)[np.array(outputs) == output], 
                np.array(Y)[np.array(outputs) == output], 
                np.array(Z)[np.array(outputs) == output], 
                label=f'Óleo {text}', 
                color='green' if output == 1 else 'red')

    xx, yy = np.meshgrid(np.linspace(min(X), max(X), 10), np.linspace(min(Y), max(Y), 10))
    zz = (-model.weights[1] * xx - model.weights[2] * yy - model.weights[0]) / model.weights[2]

    ax.plot_surface(xx, yy, zz, alpha=0.8, color='black')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title(f'Número de épocas: {model.epochs}\nEquação: z = ({model.weights[1]:.2f})x + ({model.weights[2]:.2f})y + ({model.weights[0]:.2f})')
    ax.legend()

    plt.show()

    for i in range(0, len(inputTest)):
        y = model.operation(inputTest[i])
        if(y != outputTest[i]):
            print(f"Erro no teste {i+1}!")
        else:
            if(y == -1):
                print(f"""Resultado esperado: {outputTest[i]}  |   Saída: {y}""")
            else:
                print(f"""Resultado esperado: {outputTest[i]}   |   Saída: {y}""")

def countModelTraining(c):
        print(f"""\n--------------------------------------------------
|                    Modelo {c}                    |
--------------------------------------------------\n""")

for i in range(5):
    countModelTraining(i+1)
    trainModel(0.01)
