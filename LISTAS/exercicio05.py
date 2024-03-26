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

def lista_igual(lst1, lst2):
    atual1 = lst1
    atual2 = lst2
    while atual1 is not None and atual2 is not None:
        if atual1.info != atual2.info:
            return False
        atual1 = atual1.prox
        atual2 = atual2.prox

    return atual1 is None and atual2 is None



lst1 = lista_cria()
lst1 = lista_insere(lst1, 1)
lst1 = lista_insere(lst1, 2)
lst1 = lista_insere(lst1, 3)
lst1 = lista_insere(lst1, 4)


lst2 = lista_cria()
lst2 = lista_insere(lst2, 1)
lst2 = lista_insere(lst2, 2)
lst2 = lista_insere(lst2, 3)
lst2 = lista_insere(lst2, 4)

iguais = lista_igual(lst1, lst2)
print("As listas são iguais:", iguais)

if iguais:
    print("Lista 1:")
    lista_imprime(lst1)
    print("Lista 2:")
    lista_imprime(lst2)
else:
    print("As listas não são iguais.")

