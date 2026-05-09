import re

def calcular():
    print("\nBem vindo(a) a calculadora!")
    print("Escolha a operação!")
    print("1 ~ Adição +")
    print("2 ~ Subtração -")
    print("3 ~ Multiplicação *")
    print("4 ~ Divisão /")

    while True:
        try:

            operação = int(input("Digite o número correspondente a operação desejada (1/2/3/4)"))

            if operação not in(1,2,3,4):
                raise ValueError("Operação mal-sucedida.Tente novamente")
            break
        except ValueError as e:
            print(e)

    try:
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))    

        if operação == 1:
            resultado = num1 + num2
            print(f"O resultado de {num1} ➕ {num2} é {resultado}")
        elif operação == 2:
            resultado = num1 - num2
            print(f"O resultado de {num1} ➖ {num2} é {resultado}")
        elif operação == 3:
            resultado = num1 * num2
            print(f"O resultado de {num1} ✖ {num2} é {resultado}")
        elif operação == 4:
            if num2 or num1 == 0:
                print("Divisão com 0 não funciona❌")
            else:
                resultado = num1 / num2
                print(f"O resultado de {num1} ➗ {num2} é {resultado}")
        
    except ValueError:
        print("Por favor,insira números validos.")

while True:
    calcular()
    reiniciar = input("Deseja realizar outro cálculo? (s/n)").lower()
    if reiniciar != "s":
        print("Encerrando a UCalc. Até logo!")
        break
