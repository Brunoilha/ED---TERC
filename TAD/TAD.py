class lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None


def cria_lista():
    return lista()


def insere_lista(lst,valor):
    novo_no = lista(valor)
    novo_no.prox = lst
    return novo_no

def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def lista_vazia(lst):
    return lst is None

def lista_busca(lst,valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False


lst = cria_lista()
print(lista_vazia(lst))
lst = insere_lista(lst,50)
lst = insere_lista(lst,60)
lst = insere_lista(lst,70)
lst = insere_lista(lst,80)
lista_imprime(lst)
lista_vazia(lst)


busca = lista_busca(lst,50)
if busca:
    print("achei {} " .format(busca.info))
else:
    print("nao achei")
