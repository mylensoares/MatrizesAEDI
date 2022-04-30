# Exibindo a matriz Original
def matriz_Original(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(f"{matriz[i][j]:2d}", end=" ")
        print()

# Exibindo a matriz transposta com inversão das variáveis de controle i e j 
def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range((len(matriz[0]))):
            print(f"{matriz[j][i]:2d}", end=" ")
        print()


matriz = [[9, 7, 4, 2], [10, 13, 18, 21], [33, 5, 7, 90], [23, 31, 51, 60]]

matriz_Original(matriz)
matriz_transposta(matriz)