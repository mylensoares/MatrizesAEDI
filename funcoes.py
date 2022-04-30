# Lendo Matriz da entrada padrão
def ler_matriz():
    matriz = []
    l = int(input("Informe a quantidade de linhas da matriz: "))
    c = int(input("Informe a quantidade de colunas da matriz: "))
    for i in range(l):
        linhas = []
        for j in range(c):
            elementos = int(input(f"Insira um número na Linha{i+1:2d} Coluna {j+1:2d}: "))
            linhas.append(elementos)
        matriz.append(linhas)
    return matriz

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

# Soma diagonal Principal de uma matriz 
def soma_DiagonalPrincipal(matriz):
    soma = 0
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i] == matriz[j]:
                    soma += matriz[i][j]
        print(f"A soma dos elementos da diagonal da matriz é {soma}")
    else:
        print("Não é possível somar os elementos da diagonal de uma matriz que não é quadrática")

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
#matriz = [[9, 7, 4, 2], [10, 13, 18, 21], [33, 5, 7, 90], [23, 31, 51, 60]]