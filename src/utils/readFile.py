def getInputData():
    try:
        with open("src/data/training.txt", "r") as file:
            lines = file.readlines()

        inputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 5:
                inputs.append([float(num) for num in numbers[:4]])

        return inputs

    except FileNotFoundError:
        print("Erro: Arquivo não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def getOutputData():
    try:
        with open("src/data/training.txt", "r") as file:
            lines = file.readlines()
        outputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 5:
                outputs.append(float(numbers[4]))

        return outputs

    except FileNotFoundError:
        print("Erro: Arquivo não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getTestInputData():
    try:
        with open("src/data/test.txt", "r") as file:
            lines = file.readlines()

        inputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 5:
                inputs.append([float(num) for num in numbers[:4]])

        return inputs

    except FileNotFoundError:
        print("Erro: Arquivo não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getTestOutputData():
    try:
        with open("src/data/test.txt", "r") as file:
            lines = file.readlines()
        outputs = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 5:
                outputs.append(float(numbers[4]))

        return outputs

    except FileNotFoundError:
        print("Erro: Arquivo não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []


def getSamplesData():
    try:
        with open("src/data/samples.txt", "r") as file:
            lines = file.readlines()

        samples = []

        for line in lines:
            numbers = line.strip().split()
            if len(numbers) >= 4:
                samples.append([float(num) for num in numbers])

        return samples

    except FileNotFoundError:
        print("Erro: Arquivo não foi encontrado.")
        return [], []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []
