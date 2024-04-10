
class Pilha:
    def __init__(self, tam=20):
        self.tam = tam
        self.n = 0
        self.vet = [None] * tam

def pilha_cria():
    return Pilha()

def pilha_push(p, num, operadores):
    if p.n < p.tam:
        p.vet[p.n] = num
        p.n += 1
        print("numero", num, "add")

        p.n < p.tam
        p.vet[p.n] = operadores
        p.n += 1
        print("operador", operadores, "foi add")
    else:
        print("operação salva")

## importação
from calculadora import *

if __name__ == "__main__":

    p = pilha_cria()
    
    while True:
        num = int(input("digite um numero: "))
        operadores = input("digite os operandos: ")
        if num == -1 and operadores == -1:
            break
        pilha_push(p, num, operadores)
        print(p.n)
        print(p)
        
    
    

    
