# Perceptron Neural Network

O Perceptron é um modelo de rede neural simples desenvolvido na década de 1950 por Frank Rosenblatt. Ele serve como um classificador binário, capaz de aprender a partir de exemplos e realizar previsões com base em dados de entrada. O Perceptron é fundamental para a compreensão de redes neurais mais complexas e é uma introdução importante aos conceitos de aprendizado de máquina.

Durante a fase de treinamento, o Perceptron ajusta seus pesos com base nos dados de entrada e nas saídas desejadas. Ele utiliza uma função de ativação, tipicamente uma função de ativação degrau bipolar, que transforma a combinação linear dos pesos e entradas em uma saída binária. O modelo segue a regra de Hebb, que é um princípio de aprendizado que afirma que os pesos são atualizados proporcionalmente ao produto da saída esperada e a entrada.

O Perceptron é incapaz de resolver problemas que não são linearmente separáveis. Isso significa que, se os dados de entrada não puderem ser divididos por uma linha (ou hiperplano em dimensões superiores), o modelo não conseguirá aprender a classificação correta. Um exemplo clássico é a função XOR, onde os pontos de dados não podem ser separados linearmente.

## Problema

A partir da análise de um processo de destilação fracionada de petróleo observou-se que determinado óleo poderia ser classificado em duas classes de pureza {C1 e C2} a partir da medição de três grandezas {x1, x2 e x3} que representam algumas das propriedades físico- químicas do óleo. A equipe de engenheiros e cientistas pretendem utilizar um Perceptron para executar a classificação automática destas duas classes.

Assim, baseado nas informações coletadas do processo formou-se o conjunto de treinamento tomando por convenção o valor –1 para óleo pertencente à classe C1 e o valor +1 para óleo pertencente à classe C2.

Utilizando o algoritmo supervisionado de Hebb (regra de Hebb) para classificação de padrões e assumindo a taxa de aprendizagem igual a 0,01, treine o modelo.

## Informações sobre o repositório e utilização

Este repositório contém a implementação de um algoritmo de perceptron em Python, capaz de treinar um modelo simples com base em dados fornecidos e, posteriormente, testá-lo em um conjunto de dados de teste. A implementação utiliza as seguintes bibliotecas:

- **matplotlib.pyplot** para visualização (a ser implementada)
- **numpy** para operações numéricas

O perceptron segue a regra de Hebb para treinamento, utilizando uma função de ativação degrau bipolar para atualizar os pesos.
Pré-requisitos

Para executar este código, é necessário ter o Python e as dependências necessárias instaladas. Este guia irá ajudá-lo a configurar um ambiente virtual para gerenciar suas dependências.

### Pacotes Necessários

- Python 3.6+
- numpy
- matplotlib

### Configurando o Ambiente Virtual

O uso de um ambiente virtual é uma prática recomendada para gerenciar as dependências em projetos Python. As seções a seguir mostram como criar e ativar um ambiente virtual no Windows, Linux e macOS.

### 1. Instalação do Python

Certifique-se de que você tem o Python instalado em seu sistema. Você pode baixar o Python a partir do site oficial.

### 2. Criando um Ambiente Virtual

**Windows**

1 - Abra o `Prompt de Comando` ou `PowerShell`.

2 - Navegue até o diretório do seu projeto.

3 - Crie o ambiente virtual com o comando:

```bash
python -m venv venv
```

4 - Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

**Linux e macOS**

1 - Abra o terminal.

2 - Navegue até o diretório do seu projeto.

3 - Crie o ambiente virtual com o comando:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

### 3. Instalando as Dependências

Com o ambiente virtual ativado, instale as dependências necessárias com o seguinte comando:

```bash
pip install numpy matplotlib
```

### Executando o Código

Certifique-se de que você tenha os arquivos training.txt e test.txt no diretório do projeto. Estes arquivos devem conter os dados de treinamento e teste, respectivamente.

Para executar o script, certifique-se de estar com o ambiente virtual ativado e execute:

```bash
python3 src/main.py
```

## Contribuindo

Sinta-se à vontade para contribuir para o projeto, adicionando novas funcionalidades, melhorias na documentação, ou correções.

## Licença

Este projeto está sob a licença MIT.
