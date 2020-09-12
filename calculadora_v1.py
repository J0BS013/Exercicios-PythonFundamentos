# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def soma(num1,num2):
    soma = num1 + num2
    return soma

def subtracao(num1,num2):
    subtracao = num1 - num2
    return subtracao

def multiplicacao(num1,num2):
    multiplicacao = num1 * num2
    return multiplicacao

def divisao(num1,num2):
    divisao = num1 / num2
    return divisao

def continuar():
    con = input("\nDeseja continuar? (sim/não) ")
    if con == "sim":
        calc()
    elif con == "não":
        exit()
    else:
        print("\n Opção inválida! Aplicação encerrada")

def calc():
    print("\n******************* Python Calculator ******************* \n"
          "Selecione o número da operação desejada: \n"
          "1 - Soma \n"
          "2 - Subtração \n"
          "3 - Multiplicação \n"
          "4 - Divisão \n"
          )

    opc = input("Digite sua opção: (1/2/3/4): " )
    print("\n")
    num1 =  float(input("Digite o primeiro número: "))
    num2 =  float(input("Digite o segundo número: "))

    if (opc == '1'):
        print("\n",num1, " + ",num2," = ", soma(num1,num2))
        continuar()
    elif (opc == '2'):
        print("\n",num1, " - ",num2," = ", subtracao(num1, num2))
        continuar()
    elif (opc == '3'):
        print("\n",num1, " x ",num2," = ", multiplicacao(num1, num2))
        continuar()
    elif (opc == '4'):
        print("\n",num1, " / ", num2, " = ", divisao(num1, num2))
        continuar()
    else:
        print("\nOpção inicial inválida!")
        continuar()
calc()

