produtos = dict(Bola=10, Carrinho=20, Boneca=15, Cartas=23, Pokemon=10)

apagar = str(input("Deseja apagar todos os elementos? "))

if apagar == "sim":
    produtos.clear()

print(produtos)