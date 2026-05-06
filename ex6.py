dic1 = dict(filme1=30, filme2=10, filme3=20)
dic2 = dic1.copy()

dic2.update(filme1=40, filme2=20)

print("Dicionario 1:",dic1)
print("Dicionario 2:", dic2)