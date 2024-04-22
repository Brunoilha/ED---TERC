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



