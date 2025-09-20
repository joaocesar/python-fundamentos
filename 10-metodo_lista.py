listaFilmes = ["Matrix", "Top Gun", "Interestelar", "O Poderoso Chefão", "O Senhor dos Anéis"]

# 1 - Tamanho da lista
print(len(listaFilmes))

# 2 - Buscar um item da lista pelo valor
print(listaFilmes.index("Interestelar"))

# 3 - Adicionar um item na lista
listaFilmes.append("Star Wars")
print(listaFilmes)

# 4 - Ordenar a lista
listaFilmes.sort()
print(listaFilmes)

# 5 - Remover um item da lista
listaFilmes.remove("Top Gun")
print(listaFilmes)

# 6 - Copiar uma lista para outra
novaLista = listaFilmes.copy()
print(novaLista)

# 7 - Remover todos os itens da lista
novaLista.clear()
print(novaLista)

listaNumeros = []
num = int(input("Digite o 1o. número:\n"))
listaNumeros.append(num)
num = int(input("Digite o 2o. número:\n"))
listaNumeros.append(num)
num = int(input("Digite o 3o. número:\n"))
listaNumeros.append(num)
print(listaNumeros)
print(listaNumeros[0])
print(sum(listaNumeros))
print(max(listaNumeros))
print(min(listaNumeros))
print(sorted(listaNumeros))
print(sorted(listaNumeros, reverse=True))