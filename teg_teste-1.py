
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
    n_linhas = input("digite o numero de linhas: ")
    n_colunas = input("digite o numero de colunas: ")
    n = input("preencher a matriz com qual número?  ")

    matriz = criaMatriz(int(n_linhas), int(n_colunas), int(n))
    print(matriz)