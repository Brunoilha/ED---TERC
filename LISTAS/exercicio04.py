class lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None


def lista_cria():
    return lista()

def lista_insere(lst,valor):
    novo = lista(valor)
    novo.prox = lst
    return novo

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox


def lista_vazia(lst):
    return lista is None

def lista_busca(lst,valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False

def lista_inverte(lst):
    atual = lst
    ant = None
    while atual.info is not None:
        prox = atual.prox
        atual.prox = ant
        ant = atual
        atual = prox
    return ant
    
lst = lista_cria()
print(lista_vazia(lst))
lst = lista_insere(lst,1)
lst = lista_insere(lst,3)
lst = lista_insere(lst,5)
lst = lista_insere(lst,7)
lista_imprime(lst)
lista_vazia(lst)
print("\n lista invertida")
lst = lista_inverte(lst)
lista_imprime(lst)

