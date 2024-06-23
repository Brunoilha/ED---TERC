#1
def produto(n):
    if n == 1:
        return 1
    else:
        return n * produto(n - 1)
print(produto(5)) 

#2
def imprimir(min, max):
    if min > max:
        return
    else:
        print(min)
        imprimir(min + 1, max)
imprimir(3, 7)

#3
def potencia(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * potencia(x, n - 1)
print(potencia(2, 4))  

#4
def s(n, d):
    if n == 0:
        return 0
    else:
        return s(n // 10, d + 1) + (n % 10) * 2 ** d
print(s(1100, 0)) 

#5
def calcula_soma(x, y):
    if y == 0:
        return x
    else:
        return calcula_soma(sucessor(x), predecessor(y))

#6
def busca_binaria(vet, v, inf, sup):
    if inf > sup:
        return False
    else:
        meio = (inf + sup) // 2
        if vet[meio] == v:
            return meio
        elif vet[meio] < v:
            return busca_binaria(vet, v, meio + 1, sup)
        else:
            return busca_binaria(vet, v, inf, meio - 1)
vetor = [2, 5, 7, 10, 15, 18, 22, 25, 30, 35]
print(busca_binaria(vetor, 18, 0, len(vetor) - 1)) 
print(busca_binaria(vetor, 20, 0, len(vetor) - 1))  

#7
def binario(x):
    if x == 0:
        return ''
    else:
        return binario(x // 2) + str(x % 2)

# Função para formatar a saída
def decimal_para_binario(x):
    binario_str = binario(x)
    if binario_str == '':
        return '0'
    else:
        return binario_str

# Exemplo de uso:
print(decimal_para_binario(12))  







