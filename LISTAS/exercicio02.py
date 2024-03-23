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
    return lst is None
        
def lista_separa(lst,valor):
    lista_1 = None
    lista_2 = None
    lista_atual = lst
    while lista_atual is not None:
        if lista_atual.info == valor:
            break
        lista_1 = lista_insere(lista_1, lista_atual.info)
        lista_atual = lista_atual.prox
        
    if lista_atual is None:
        return lst, None
        
    lista_atual = lista_atual.prox
    
    while lista_atual is not None:
        lista_2 = lista_insere(lista_2, lista_atual.info)
        lista_atual = lista_atual.prox
        
    return lista_1,lista_2
        
lst = lista_cria()
print(lista_vazia(lst))
    
lst = lista_insere(lst, 2)
lst = lista_insere(lst, 4)
lst = lista_insere(lst, 8)
lst = lista_insere(lst, 10)
lst = lista_insere(lst, 12)
print("original")
lista_imprime(lst)
    
lista_1, lista_2 = lista_separa(lst, 8)

print("\n antes")
lista_imprime(lista_1)

print("\n depois")
lista_imprime(lista_2)
        
