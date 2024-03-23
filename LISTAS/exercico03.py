class lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None

def lista_cria():
    return lista()

def lista_insere(lst,valor):
    atual = lst
    novo = lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def lista_vazia(lst):
    return lst is None

def lista_marge(lst1, lst2):
    if lista_vazia(lst1):
        return lst2
    if lista_vazia(lst2):
        return lst1

    lista_junta = lista()
    atual = lista_junta

    while lst1 is not None or lst2 is not None:
        if lst1 is not None:
            atual.prox = lst1
            atual = atual.prox
            lst1 = lst1.prox
        if lst2 is not None:
            atual.prox = lst2
            atual = atual.prox
            lst2 = lst2.prox

    return lista_junta.prox

lst1 = lista_cria()
lst1 = lista_insere(lst1, 5)
lst1 = lista_insere(lst1, 4)
lst1 = lista_insere(lst1, 3)
lst1 = lista_insere(lst1, 2)
lst1 = lista_insere(lst1, 1)

lst2 = lista_cria()
lst2 = lista_insere(lst2, 10)
lst2 = lista_insere(lst2, 9)
lst2 = lista_insere(lst2, 8)
lst2 = lista_insere(lst2, 7)
lst2 = lista_insere(lst2, 6)

print("primeira lista: ")
lista_imprime(lst1)

print("segunda lista: ")
lista_imprime(lst2)

junto = lista_marge(lst1,lst2)
print("lista junta: ")
lista_imprime(junto)
