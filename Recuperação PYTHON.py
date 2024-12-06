""" Sistema de Gerenciamento de Hotel

Objetivo: Desenvolver um programa em Python que permita gerenciar um hotel,
utilizando apenas estruturas de repetição (como for e while) e estruturas de condição (if, elif, else).

Descrição do Sistema:
    ○ Cadastro de hóspedes 5 (nome, número do quarto, data de entrada e saída).
    ○ Consulta de quartos disponíveis.
    ○ Registro de saída de hóspedes.
    ○ Listagem de hóspedes cadastrados. """

# Variáveis para o cadastro
nome1, nome2, nome3, nome4, nome5 = "", "", "", "", ""
quarto1, quarto2, quarto3, quarto4, quarto5 = "", "", "", "", ""
entrada1, entrada2, entrada3, entrada4, entrada5 = "", "", "", "", ""
saida1, saida2, saida3, saida4, saida5 = "", "", "", "", ""

# Menu principal
while True: # Loop para mostrar o menu a cada rodada após o cadastro
    print("\n1- Cadastrar Hóspede")
    print("2- Consultar Quartos Disponíveis")
    print("3- Registrar Saída de Hóspede")
    print("4- Listar Hóspedes Cadastrados")
    print("5- Sair")
    escolha = int(input("Escolha uma opção: "))
    
# Cadastrar hóspedes
    if escolha == 1: 
        if nome1 == "": 
        # Verifica variável para cadastrar usuário, se sim, continua no cadastro no bloco, caso não, pula para o próximo bloco
            nome1 = input("Nome: ") 
            quarto1 = 1 
            # Variável servindo como contador para verificar a disponibilidade dos quartos
            print("Você está no quarto 1")
            entrada1 = int(input("Data de entrada: "))
            saida1 = int(input("Data de saída: ")) 
            print("Cadastro realizado com sucesso!") 
        elif nome2 == "": 
            nome2 = input("Nome: ") 
            quarto2 = 2
            print("Você está no quarto 2")
            entrada2 = int(input("Data de entrada: ")) 
            saida2 = int(input("Data de saída: ")) 
            print("Cadastro realizado com sucesso!") 
        elif nome3 == "": 
            nome3 = input("Nome: ") 
            quarto3 = 3
            print("Você está no quarto 3")
            entrada3 = int(input("Data de entrada ")) 
            saida3 = int(input("Data de saída: ")) 
            print("Cadastro realizado com sucesso!")
        elif nome4 == "": 
            nome4 = input("Nome: ")
            quarto4 = 4
            print("Você está no quarto 1")
            entrada4 = int(input("Data de entrada: "))
            saida4 = int(input("Data de saída: ")) 
            print("Cadastro realizado com sucesso!") 
        elif nome5 == "": 
            nome5 = input("Nome: ") 
            quarto5 = 5
            print("Você está no quarto 5")
            entrada5 = int(input("Data de entrada: "))
            saida5 = int(input("Data de saída: "))
            print("Cadastro realizado com sucesso!") 
        else: print("Limite de cadastrados atingido.")

# Consultar quartos disponíveis
    elif escolha == 2:
        if quarto1 == "":
            print("Quarto 1 disponível.")
        else:
            print("Quarto 1 indisponível.")
        if quarto2 == "":
            print("Quarto 2 disponível.")
        else:
            print("Quarto 2 indisponível.")
        if quarto3 == "":
            print("Quarto 3 disponível.")
        else:
            print("Quarto 3 indisponível.")
        if quarto4 == "":
            print("Quarto 4 disponível.")
        else:
            print("Quarto 4 indisponível.")
        if quarto5 == "":
            print("Quarto 5 disponível.")
        else:
            print("Quarto 5 indisponível.")
        if quarto1 != "" and quarto2 != "" and quarto3 != "" and quarto4 != "" and quarto5 != "":
            print("Nenhum quarto disponível.")
        elif quarto1 == "" and quarto2 == "" and quarto3 == "" and quarto4 == "" and quarto5 == "":
            print("Todos os quartos estão disponíveis.")

# Registro de saída de hóspedes
    elif escolha == 3:
        # Variável para usar os quartos como referência de saída
        quarto = int(input("Digite o número do quarto do hóspede para registrar a saída: "))
        if quarto == 1:
            nome1, quarto1, entrada1, saida1 = "", "", "", "" # Após confirmação de saída, as demais variáveis se tornam vazias ""
            print("Saída registrada.")
        elif quarto == 2:
            nome2, quarto2, entrada2, saida2 = "", "", "", ""
            print("Saída registrada.")
        elif quarto == 3:
            nome3, quarto3, entrada3, saida3 = "", "", "", ""
            print("Saída registrada.")
        elif quarto == 4:
            nome4, quarto4, entrada4, saida4 = "", "", "", ""
            print("Saída registrada.")
        elif quarto == 5:
            nome5, quarto5, entrada5, saida5 = "", "", "", ""
            print("Saída registrada.")
        else:
            print("Número do quarto não encontrado.")

# Listagem de hóspedes cadastrados
    elif escolha == 4:
        if nome1 != "":
            print(f"Nome: {nome1}, Quarto: {quarto1}, Entrada: {entrada1}, Saída: {saida1}") # Busca as variáveis no registro de cadastro e imprime console
        if nome2 != "":
            print(f"Nome: {nome2}, Quarto: {quarto2}, Entrada: {entrada2}, Saída: {saida2}")
        if nome3 != "":
            print(f"Nome: {nome3}, Quarto: {quarto3}, Entrada: {entrada3}, Saída: {saida3}")
        if nome4 != "":
            print(f"Nome: {nome4}, Quarto: {quarto4}, Entrada: {entrada4}, Saída: {saida4}")
        if nome5 != "":
            print(f"Nome: {nome5}, Quarto: {quarto5}, Entrada: {entrada5}, Saída: {saida5}")
        if nome1 == "" and nome2 == "" and nome3 == "" and nome4 == "" and nome5 == "":
            print("Nenhum hóspede cadastrado.")

# Sair do sistema
    elif escolha == 5:
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 5.")
