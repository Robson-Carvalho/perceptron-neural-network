# Perceptron Neural Network 

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

## Configurando o Ambiente Virtual

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
python3 main.py
```

## Contribuindo

Sinta-se à vontade para contribuir para o projeto, adicionando novas funcionalidades, melhorias na documentação, ou correções.

## Licença

Este projeto está sob a licença MIT.