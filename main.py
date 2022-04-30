import menu
import funcoes

matriz = funcoes.ler_matriz()
print("Matriz definida com sucesso!")

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
    