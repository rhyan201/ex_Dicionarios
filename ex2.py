produtos = dict(Bola=10, Carrinho=20, Boneca=15)

print(produtos)

chave = str(input("Digite o nome do produto que deseja alterar: "))
print("O valor do produto selecionado(",chave,") é de:", produtos.get(chave))

valor_novo = int(input("Digite o novo valor do produto que deseja alterar: "))
produtos.update({chave: valor_novo})

print(produtos)