import matplotlib.pyplot as plt
import numpy as np

class Perceptron:
    # Inicialização com valores aleatórios de pesos aleatórios e baia 
    def __init__(self):
        self.weights = np.random.uniform(-1, 1, 3)
        self.bias = np.random.uniform(-1, 1)
    
    # Treinamento 
    def training(self, inputs, outputs, learning_rate, epochs):
        self.inputs = inputs # Entradas 
        self.outputs = outputs # Saídas esperadas
        self.learning_rate = learning_rate # Taxa de aprendizagem
        self.epochs = epochs # Número de épocas
        
        for _ in range(epochs):
            for i in range(len(inputs)):
                deltaWeight = learning_rate * inputs[i] * outputs[i]
                deltaBias = learning_rate * outputs[i]
                self.weights[i] += deltaWeight
                self.bias = self.bias + deltaBias
                
        

        
        
        
        