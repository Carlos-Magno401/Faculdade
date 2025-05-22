#Ordenação
 #Alguns dos algoritmos mais conhecidos:
 #- Bubble sort (ordenação por flutuação); fazendo comparações 2 a 2 e levando o maior elemento até o final da lista
 #- Insertion sort (ordenação por inserção);  organizando como se estivesse pegando uma carta e botando ela no lugar, verificando se ela é maior que a adjacente
 #- Selection sort (ordenação por seleção); já tem todas as cartas, procura a maior e coloca no final
 #- Merge sort (ordenação por mistura): divide a lista pela metade, organiza ela e depois mescla de volta 
 #- Quicksort; escolhe um pivô na lista, e coloca todos que são menores pra baixo e todos que são maiores pra cima


#Bubble sort
def bubble_sort(lista):
    n=len(lista)
    for j in range (n-1):
        for i in range (n-1):
            if lista[i] > lista[i+1]:
                #troca de elementos nas posiçãoes i e i+1
                lista[i], lista[i+1] = lista [i+1], lista[i]

#Insertion sort
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista [j+1] = lista[j]
            j = j-1
        lista [j+1] = chave

#Selection sort
def selection_sort(lista):
    n = len(lista)
    for j in range (n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j]=lista[min_index]
            lista[min_index] = aux

#Merge Sort
def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge (lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range (inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

#Quick Sort
def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim= len(lista) - 1
    if inicio < fim:
        p = partition (lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range (inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista [i] = lista[i], lista[j]
            i = i+1
    lista[i], lista[fim] = lista[fim], lista[j]
    return i