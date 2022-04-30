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

# Soma diagonal Principal de uma matriz 4x4
def soma_DiagonalPrincipal(matriz):
    for i in matriz:
        pri_elemento = matriz[0][0]
        seg_elemento = matriz[1][1]
        ter_elemento = matriz[2][2]
        qua_elemento = matriz[3][3]
        soma = pri_elemento + seg_elemento + ter_elemento + qua_elemento
    return print(f"A soma a digonal a matriz é {soma}")

# Exibindo apenas os números pares da matriz
def pares_matriz(matriz):
    pares = []
    for i in range(len(matriz)):
        for j in range((len(matriz[0]))):
            if matriz[i][j] % 2 == 0:
                pares.append(matriz[i][j])
    print("="*30, "PARES" ,"="*30)
    return print(f"Os Números Pares presentes na matriz são: {pares}")

# Exibindo apenas os números ímpares da matriz
def impares_matriz(matriz):
    impares = []
    for i in range(len(matriz)):
        for j in range((len(matriz[0]))):
            if matriz[i][j] % 2 != 0:
                impares.append(matriz[i][j])
    print("="*30, "ÍMPARES" ,"="*30)
    return print(f"Os Números Ímpares presentes na matriz são: {impares}")

