import menu
import funcoes

matriz = [[9, 7, 4, 2], [10, 13, 18, 21], [33, 5, 7, 90], [23, 31, 51, 60]]

while True:
    print("="*60)
    menu.menu_principal()
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 0:
        print("Sistema Finalizado!")
        break
    elif opcao == 1:
        funcoes.matriz_Original(matriz)
    elif opcao == 2:
        funcoes.matriz_transposta(matriz)
    elif opcao == 3:
        funcoes.soma_DiagonalPrincipal(matriz)
    elif opcao == 4:
        funcoes.pares_matriz(matriz)
    elif opcao == 5:
        funcoes.impares_matriz(matriz)
    else:
        print("Valor inválido, tente novamente")
    