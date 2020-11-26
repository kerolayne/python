
def criaMatriz(n_lin, n_col, n):
    matriz=[]

    for i in range(n_lin):
        linha = []
        for i in range(n_col):
            linha += [n]

        matriz += [linha]

    return matriz

#def leMatriz(pos_l, ):

def main():
    n_vertices = input("digite o numero de linhas: ")
   
    n = input("preencher a matriz com qual número?  ")

    matriz = criaMatriz(int(n_vertices), int(n_vertices), int(n))
    print(matriz)
    
if __name__ == "__main__":
    main()
