cidade1 = input("Digite o nome da primeira cidade: ")
cidade2 = input("Digite o nome da segunda cidade: ")
cidade3 = input("Digite o nome da terceira cidade: ")

cidades = (cidade1, cidade2, cidade3)

print(cidades)  # Exibe a tupla completa
print(cidades[0])  # Exibe a primeira cidade
print(cidades[-1])  # Exibe a ultima cidade
print(len(cidades))  # Exibe o tamanho da tupla
print(cidades.count(cidade1))  # Conta quantas vezes a primeira cidade aparece na tupla
print(cidades.index(cidade2))  # Exibe o índice da segunda cidade