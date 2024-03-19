class lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None

def lista_cria():
    return lista()

def lista_insere(lst, valor):
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

def lista_busca(lst,valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False

def lista_retira(lst,valor):
    if lst is None:
        return None
    
    if lst.info == valor:
        return lst.prox

    x = lst
    atual = lst.prox
    while atual is not None:
        if atual.info == valor:
            x.prox = atual.prox
            return lst
        x = atual
        atual = atual.prox
    return lst


lst = lista_cria()
print(lista_vazia(lst))
lst = lista_insere(lst,50)
lst = lista_insere(lst,20)
lst = lista_insere(lst,90)
lst = lista_insere(lst,30)
lst = lista_insere(lst,250)
lista_imprime((lst))
lista_vazia(lst)
lst = lista_retira(lst, 20)

busca = lista_busca(lst, 50)
if busca:
    print("achei {}".format((busca.info)))
else:
    print("nao achei")

retira = lista_retira(lst,20)
print("dps da remocao:")
lista_imprime(lst)
