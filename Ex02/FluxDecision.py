print(f"*Optimized Customer System*")
print(f"-" * 30)  # Separador/organizador de boa leitura ao usuário do sistema
NameUser = str(input(f"Insira o nome do Usuário: "))
print(f"-" * 30)  # Separador/organizador de boa leitura ao usuário do sistema
print(f"Seja Bem-Vindo ao Optimized Customer System, Sr(a) {NameUser}")

# Inicia o loop para verificar as condições de elegibilidade
while True:
    print(f"-" * 30)  # Separador/organizador de boa leitura ao usuário do sistema
    AgeUser = int(input(f"Insira sua idade: "))
    IncomeUser = input(f"Insira sua Renda Mensal: R$")
    ArrearUser = str(input(f"Possui dívidas pendentes? (sim/não): "))
    print(f"-" * 30)  # Separador/organizador de boa leitura ao usuário do sistema
    
    # Verifica se a idade é maior ou igual a 18
    if AgeUser >= 18:
        # Substitui a vírgula por ponto e converte a renda para float
        IncomeUser = IncomeUser.replace(",", ".")
        IncomeUser = float(IncomeUser)
        
        # Verifica se a renda é maior ou igual a R$ 2.500,00
        if IncomeUser >= 2500:
            
            # Valida a entrada sobre dívidas pendentes
            while ArrearUser.lower() not in ["não", "nao", "not", "negativo", "false", "n", "sim", "yes", "afirmativo", "confirmo", "true", "s"]:
                # Caso o usuário insira algo inválido
                print("Resposta inválida! Por favor, insira 'sim' ou 'não'.")
                ArrearUser = str(input(f"Possui dívidas pendentes? (sim/não): "))
            # Se o cliente não tiver dívidas pendentes, ele é elegível para continuar no sistema
            if ArrearUser.lower() in ["não", "nao", "not", "negativo", "false", "n"]:
                print(f"O Sr(a) {NameUser}, está elegível")
                break  # Finaliza o loop
            else:
                # Se o cliente tiver dívidas pendentes, voltará ao loop
                print(f"Cliente não elegível, motivo: Dívidas Pendentes")
        else:
            # Se a renda for insuficiente, voltará ao loop
            print(f"Cliente não elegível, motivo: Renda Mensal Insuficiente")
    else:
        # Se a idade for insuficiente, voltará ao loop
        print(f"Cliente não elegível, motivo: Idade Insuficiente")