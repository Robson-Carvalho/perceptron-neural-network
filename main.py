import matplotlib.pyplot as plt
import numpy as np

class Perceptron:
    # Inicialização os pesos e o limiar com values aleatórios
    def __init__(self):
        self.weights = np.random.uniform(-1, 1, 3)
        self.bias = np.random.uniform(-1,1)

    # Função de ativação degrau bipolar
    def bipolarStepActivationFunction(self, u):
        if u >= 0:
            return 1
        return -1

    # Treinamento
    def training(self, inputs, outputs, learning_rate, epochs):
        self.inputs = inputs  # Entradas
        self.outputs = outputs  # Saídas esperadas
        self.learning_rate = learning_rate  # Taxa de aprendizagem
        self.epochs = epochs  # Número de épocas

        for _ in range(epochs):
            for i in range(len(inputs)):
                x = inputs[i]  # uma lista de amostra, nesse caso, x¹, x² e x³ da posição i.

                u = (np.dot(x, self.weights) + self.bias)  # Somatório de x*w somado ao limiar 

                y = self.bipolarStepActivationFunction(u) # Função de ativação

                # Se y for diferente da saída deseja, atualizamos os pesos e limiar 
                if y != outputs[i]:
                    error = (outputs[i] - y)
                    self.weights[0] += (learning_rate * error * inputs[i][0])
                    self.weights[1] += (learning_rate * error * inputs[i][1])
                    self.weights[2] += (learning_rate * error * inputs[i][2])
                    self.bias += (learning_rate * error * -1)


    # Função de operação para classificar amostras após o treinamento
    def operation(self, inputs):
        u = (np.dot(inputs, self.weights) + self.bias)

        y = self.bipolarStepActivationFunction(u)
        
        return y

        
inputs = []
outputs = []  

with open('training.txt', 'r') as file:
    for line in file:
        values = line.split()
        
        if len(values) >= 5:  
            data = [float(values[i]) for i in range(1, 4)]  
            inputs.append(data)  
            outputs.append(float(values[4]))

model = Perceptron()
model.training(inputs, outputs, 0.01, 100)

tests = []
results = []  

with open('test.txt', 'r') as file:
    for line in file:
        values = line.split()
        
        if len(values) >= 5:  
            data = [float(values[i]) for i in range(1, 4)]  
            tests.append(data)  
            results.append(float(values[4]))

for i in range(0, len(tests)):
    v = model.operation(tests[i])
    print(f"Teste {i+1}")
    print(f"Saida: {v}")
    print(f"Resultado esperado: {results[i]}\n")



