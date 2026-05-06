dicionario = dict(Banana = 10, Maçã = 20, Kiwi = 30, Melão = 35)
print(dicionario)

remove = input("Digite o nome de uma chave para remover: ")
dicionario.pop(remove)
print("A chave removida foi: ", remove)

print("Uma chave aleatória será removida: )")

remove2 = dicionario.popitem()
print("A chave removida foi: ", remove2)
print(dicionario)

qtd_dados = int(input("Digite a quantidade de dados novos a serem adicionados: "))

for i in range(qtd_dados):
    chave = input("Digite o nome do chave: ")
    valor = input("Digite o valor do chave: ")
    dicionario[chave] = valor

print(dicionario)