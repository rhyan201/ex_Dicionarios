usuarios = {"Ana": 10, "Ricardo": 20, "Matheus": 25}

while True:
    print("\nFunções:")
    print("1 - Visualizar usuários")
    print("2 - Buscar usuário")
    print("3 - Adicionar usuário")
    print("4 - Atualizar idade de usuário")
    print("5 - Remover usuário")
    print("6 - Remover o ultímo elemento inserido")
    print("7 - Criar cópia do dicionário")
    print("8 - Inicializar um novo dicionário")
    print("9 - Atualizar o dicionário principal utilizando de um dicionário novo")
    print("10 - Limpar os dados do sistema")
    print("11 - Criar dicionário a partir de Tuplas")
    print("12 - Sair")

    opcao = int(input("Selecione uma opção: "))
    if opcao>=1 or opcao<=12:
        if opcao == 1:
            print(usuarios.keys())
            print(usuarios.values())
            print(usuarios.items())
            print("Voltando ao menu")

        elif opcao == 2:
            nome = input("Qual nome de usuário deseja buscar? ")
            if nome in usuarios:
                print(usuarios[nome])
            else:
                print("Usuário não encontrado")

        elif opcao == 3:
            nome = str(input("Digite o nome: "))
            idade = int(input("Digite a idade: "))
            usuarios[nome] = idade
            print(usuarios)

        elif opcao == 4:
            print(usuarios)
            nome = str(input("Digite o nome: "))
            if nome in usuarios:
                idade = int(input("Qual a nova idade: "))
                usuarios.update({nome: idade})
                print(usuarios)
            else:
                print("Usuário não encontrado")

        elif opcao == 5:
            print(usuarios)
            nome = input("Digite o nome do usuário a ser removido: ")
            if nome in usuarios:
                usuarios.pop(nome)
                print(usuarios)
            else:
                print("Usuário não encontrado")

        elif opcao == 6:
            print(usuarios)
            usuarios.popitem()
            print(usuarios)

        elif opcao == 7:
            print(usuarios)
            copia_usuarios = usuarios.copy()
            nome = str(input("Digite o nome da chave a ser alterada na cópia: "))
            if nome in usuarios:
                idade = int(input("Qual a nova idade: "))
                copia_usuarios.update({nome: idade})
                print(usuarios)
            else:
                print("Usuário não encontrado")
            print(copia_usuarios)

        elif opcao == 8:
            qtd = int(input("Digite a quantidade de elementos a serem adicionados no novo dicionário: "))
            for i in range(qtd):
                novo_dicionario = {}
                chave1 = input("Digite o nome do usuário a ser adicionada: ")
                valor1 = input("Digite a idade do usuário a ser adicionado: ")
                novo_dicionario[chave1] = valor1

        elif opcao == 9:
            qtd = int(input("Digite a quantidade de elementos a serem adicionados no novo dicionário: "))
            for i in range(qtd):
                novo_dicionario = {}
                chave2 = input("Digite o nome do usuário a ser adicionada: ")
                valor2 = input("Digite a idade do usuário a ser adicionado: ")
                novo_dicionario[chave2] = valor2
                print(novo_dicionario)
                usuarios.update(novo_dicionario)
                print(usuarios)

        elif opcao == 10:
            confirm = str(input("Você realmente deseja apagar os dados do sistema? "))
            if confirm == "Sim" or confirm == "sim":
                usuarios.clear()
                print("Excluindo os dados do sistema...")
                print(usuarios)
            else:
                print("Voltando ao menu...")

        elif opcao == 11:
            lista_tupla = []
            qtd1 = int(input("Qual a quantidade de tuplas a serem criadas: "))
            for i in range(qtd1):
                chave3 = input("Digite o nome da tupla a ser adicionada: ")
                valor3 = input("Digite a valor da tupla a ser adicionado: ")
                lista_tupla.append((chave3, valor3))
            dicionario3 = dict(lista_tupla)
            print("\n Dicionário criado: ")
            print(dicionario3)

        elif opcao == 12:
            print("Aplicativo encerrado")
            break
    else:
        break