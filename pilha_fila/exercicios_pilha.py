#exercicio 1  
class Pilha:
    def __init__(self, max_tam):
        self.max_tam = max_tam
        self.n = 0 
        self.vet = []
        
def pilha_cria(max_tam):
    return Pilha(max_tam)

def pilha_push(p, valor):
    if p.n < p.max_tam:
        p.vet.append(valor) 
        p.n += 1
        total = p.n
    else:
        print("cheio")
    print(total)
    
max_tam = 5  
p = pilha_cria(max_tam)

pilha_push(p, 5)
pilha_push(p, 8)
pilha_push(p, 20)

#exercicio 2
class Pilha:
    def __init__(self, max_tam):
        self.max_tam = max_tam
        self.vet = []
        self.n = 0

def pilha_vazia(p):
    return p.n == 0

def pilha_max(p):
    return p.n == p.max_tam

def push(p, v):
    if pilha_max(p):
        print("pilha cheia")
    else:
        p.vet.append(v)
        p.n += 1
    print("Pilha:", p.vet)

def pop(p):
    if pilha_vazia(p):
        print("pilha vazia")
        return None
    else:
        p.n -= 1
        removido = p.vet.pop()

        print("Pilha:", p.vet)
        return removido

print("A):")
P = Pilha(6)
push(P, 4)
push(P, 3)
pop(P)
push(P, 8)
pop(P)

print("B): ")
X = Pilha(6)
push(X,3)
pop(X)
pop(X)
push(X,4)

print("B_ii ): ")
Z = Pilha(6)
push(Z, 1)
pop(Z),
push(Z, 2),
push(Z, 3),
push(Z, 4),
push(Z, 5),
push(Z, 6),
push(Z, 7),
push(Z, 8)

#exercico 4
class Pilha:
    def __init__(self, max_tam):
        self.max_tam = max_tam
        self.vet = []
        self.n = 0

def pilha_vazia(p):
    return p.n == 0

def pilha_max(p):
    return p.n == p.max_tam

def push(p, v):
    if pilha_max(p):
        print("pilha cheia")
    else:
        p.vet.append(v)
        p.n += 1
    print("Pilha:", p.vet)

def pop(p):
    if pilha_vazia(p):
        print("pilha vazia")
        return None
    else:
        p.n -= 1
        removido = p.vet.pop()

        print("Pilha:", p.vet)
        return removido
def esvazia(p):
    while not pilha_vazia(p):
        pop(p)
      
p = Pilha(10)
push(p,20)
push(p,35)
push(p,5)
x = esvazia(p)
print("vazio")
print(x)

#exercicio 3
class Pilha:
    def __init__(self, max_tam):
        self.max_tam = max_tam
        self.vet = []
        self.n = 0

    def pilha_vazia(self):
        return self.n == 0

    def pilha_max(self):
        return self.n == self.max_tam

    def push(self, v):
        if self.pilha_max():
            print("pilha cheia")
        else:
            self.vet.append(v)
            self.n += 1

    def pop(self):
        if self.pilha_vazia():
            print("pilha vazia")
            return None
        else:
            self.n -= 1
            return self.vet.pop()

    def tamanho(self):
        return self.n

    def topo(self):
        if self.pilha_vazia():
            print("pilha vazia")
            return None
        else:
            return self.vet[-1]


P = Pilha(10)
P.push(4)
P.push(3)

# a) Retornar o número de objetos na pilha
print("numero do obj na pilha:", P.tamanho())

# b) Retornar o objeto no topo da pilha
print("obj topo da pilha:", P.topo())


