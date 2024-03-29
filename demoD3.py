from knn_utils import *


# Students: Carlos Henrique Ponciano da Silva & Vinicius Luis da Silva

def execute():
    print('\nQuestão 3')
    _data = read('grupoDados3')
    _grupoTrain, _trainRots, _grupoTest, _testRots = separate_dataset(_data)

    # Q3.1: Aplique o kNN ao problema usando k = 1. Qual é a acurácia na classificação?
    # A acurácia é de 58%
    _predicted_label_k1 = predict(_grupoTrain, _trainRots, _grupoTest, 1)
    _accuracy = accuracy(_predicted_label_k1, _testRots)
    print(f'Q3.1. Acurácia do K = 1: {_accuracy}')

    # Q3.2: A acurácia pode ser igual a 92% com o kNN. Descubra por que o resultado atual é muito menor.
    # Ajuste o conjunto de dados ou k de tal forma que a acurácia se torne 92% e explique o que você fez e
    # por quê?
    # Foi necessário ir incrementando K para encontrar a acuracia de 92%, onde K deve ser igual a  7
    _k, _prediced = get_quantity_groups(_grupoTrain, _trainRots, _grupoTest, _testRots, 0.92)
    print(f'Q3.2. K = {_k}')

    plot(_data['grupoTest'], [_testRots, _predicted_label_k1, _prediced], ['Original', f'K = 1', f'Acurácia de 92% - K = {_k}'], 'Questão 3')