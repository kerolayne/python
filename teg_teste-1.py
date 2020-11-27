

def criaMatriz(n_vertices, n):
    matriz=[]

    for i in range(n_vertices):
        linha = []
        for i in range(n_vertices):
            linha += [n]

        matriz += [linha]

    return matriz

def inserePosMatriz(linha, coluna, n_vertices):
    i = 0
    for i in range(n_vertices):
        if i == linha:
            for i in range(n_vertices):
                if i == coluna:
                    linha += 1

    return matriz


def main():
    n_vertices = input("digite o numero de vertices: ")
   
    n = input("preencher a matriz com qual número?  ")

    matriz = criaMatriz(int(n_vertices), int(n))
    print(matriz)

    linha = input("vertice 1: ")
    coluna = input("vertice 2: ")

    matrizA = inserePosMatriz(int(linha), int(coluna), int(n), matriz)
    print(matrizA)
    
if __name__ == "__main__":
    main()
