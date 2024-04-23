#exercicio 1 
def imprimir_fila_vetor(fila_vetor, inicio, tamanho):
    print("Fila como vetor (fila circular):")
    if tamanho == 0:
        print("A fila está vazia")
    else:
        for i in range(tamanho):
            indice = (inicio + i) % len(fila_vetor)
            print(fila_vetor[indice], end=" ")
        print()


def imprimir_fila_lista(fila_lista):
    print("Fila como lista:")
    if not fila_lista:
        print("A fila está vazia")
    else:
        for item in fila_lista:
            print(item, end=" ")
        print()


def main():
   
    fila_lista = []

   
    fila_lista.append(1)
    fila_lista.append(2)
    fila_lista.append(3)
    fila_lista.append(4)
    fila_lista.append(5)

 
    inicio = 0

    tamanho_fila = len(fila_lista)

  
    imprimir_fila_vetor(fila_lista, inicio, tamanho_fila)

    
    imprimir_fila_lista(fila_lista)

if __name__ == "__main__":
    main()

#exercicio 3
def fila_cria(tam):
    tam
    print("Eu funciono 100%")
def fila_insere(f, v):
    f, v
    print("Eu funciono 100%")
def fila_retira(f):
    f
    print("Eu funciono 100%")
def fila_vazia(f):
    f
    print("Eu funciono 100%")
def fila_frente(f):
    f
    print("Eu funciono 100%")


def ordena_filas(f1, f2):
    fila_resultante = fila_cria(f1.tamanho() + f2.tamanho())  

   
    while not fila_vazia(f1) and not fila_vazia(f2):
      
        if fila_frente(f1) <= fila_frente(f2):
            fila_insere(fila_resultante, fila_retira(f1))  
        else:
            fila_insere(fila_resultante, fila_retira(f2))  #

   
    while not fila_vazia(f1):
        fila_insere(fila_resultante, fila_retira(f1))

   
    while not fila_vazia(f2):
        fila_insere(fila_resultante, fila_retira(f2))

    return fila_resultante
  
#exercicio 2

def combina_filas(f_res, f1, f2):
    while f1 or f2:  
        if f1:  
            f_res.append(f1.pop(0))  
        if f2:  
            f_res.append(f2.pop(0))  

