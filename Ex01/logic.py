NumIntArray = []
NumIntUser = 0
Y = 0
Z = 0
# Enquanto a condição for verdadeira, deve-se manter
while True:
    NumIntUser = input(f"Entre com somentes números INTEIROS e separados por SPACE:")
    #Condição para ver se há mais de um número
    if " " in NumIntUser:
        #Se houver números inteiros, a condição deve se seguir
        try:
            NumIntArray = list(map(int, NumIntUser.split()))
            #Separador textual para que haja coesão
            print(f"-" * 40)
            #exibição do array inteiro
            print(f"Array com números inseridos: {NumIntArray}")
            #condicional para o cálculo do pares e Ímpares
            for X in NumIntArray:
                if X % 2 == 0:
                    Y += X
                else:
                    Z += X
            #exibição dos resultados
            print(f"A soma dos números Pares são: {Y}")
            print(f"A soma dos números Impares são: {Z}")
            break
        except ValueError:
            #Caso haja números fracionados
            print(f"Por favor, somente números inteiros para o exercício")
    else:
        #Condição resultante para que a soma dos números dê certo
        print(f"Por favor, Insira mais de um número")
