import copy


lista = [1, 2, 3]

#copia rasa
copia_1 = lista
copia_2 = lista[:]
copia_3 = lista.copy()
copia_4 = list(lista)
copia_5 = copy.copy(lista)

#copia profunda
copia_6 = copy.deepcopy(lista)