notas = dict(Pedro=10, Matheus=7, Maria=5, Isabelli=10, Rhyan=8)

searchAl = input("Qual o nome do aluno? ")

if searchAl in notas:
    notas.get(searchAl)
    print("A nota do aluno", searchAl, "é de", notas.get(searchAl))
else:
    print("Aluno não encontrado")