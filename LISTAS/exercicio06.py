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

def lista_copia(lst):
    novo_no = lista(lst.info)
    atual = lst
    copia_lista = novo_no
    while atual.prox is not None:
        copia_lista.prox = lista(atual.prox.info)
        atual = atual.prox
        copia_lista = copia_lista.prox
    return novo_no

lst = lista_cria()
lst = lista_insere(lst, 1)
lst = lista_insere(lst, 2)
lst = lista_insere(lst, 3)
lst = lista_insere(lst, 4)


copia = lista_copia(lst)
print("lista copiada com sucesso: ", copia)
lista_imprime(copia)
