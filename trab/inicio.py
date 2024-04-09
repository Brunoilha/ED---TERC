class Pilha:
    def __init__(self, tam=20):
        self.tam = tam
        self.n = 0
        self.vet = [None] * tam


def pilha_cria():
    return Pilha()

def pilha_push(p, o):
    if p.n < p.tam:
        p.vet[p.n] = o
        p.n += 1
        print("numero", o, "add")
    else:
        print("pilha cheia")

def pilha_cria_operador():
    return Pilha()



def pilha_pop(p):
    if p.n > 0:
        o = p.vet[p.n - 1 ]
        print("retirado da pilha", o)
    else:
        print("numero inexistente")
    return o

def pilha_push_operador(p,operadores):
    if p.n < p.tam:
        p.vet[p.n] = operadores
        p.n += 1
        print("operador", operadores, "foi add")
    else:
        print("nao foi possivel add")



from calculadora import *

if __name__ == "__main__":
    p = pilha_cria()
    print("criando pilha")

    pilha_push(p, 5)


    pilha_push(p, 15)


    pilha_pop(p)


    p = pilha_cria_operador()
    pilha_push_operador(p, "/")










