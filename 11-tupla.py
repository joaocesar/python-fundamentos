# Tupla é definida por parênteses ()
# Pode conter diferentes tipos de dados
# Não pode ser alterada (imutável)

# Pode ser acessada por índices como listas
filmesTrupla = ("Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interstellar")

print(filmesTrupla)
print(type(filmesTrupla))

# 1 - Buscar os dois primeiros filmes da tupla
print(filmesTrupla[:2])

# 2 - Buscar o ultimo filme da tupla
print(filmesTrupla[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmesTrupla[:3]) 

# 4 - Buscar filmes a partir de uma determinada posição
print(filmesTrupla[1:4])
print(filmesTrupla[2:])

# 5 - Outros exemplos de fatiamento (slicing)
print(filmesTrupla[::2])  # Pula de 2 em 2
print(filmesTrupla[::-1])  # Inverte a tupla
print(filmesTrupla[-1:-4:-1])  # Inverte a tupla parcialmente
print(len(filmesTrupla))  # Tamanho da tupla
print(filmesTrupla.count("Inception"))  # Conta quantas vezes o item aparece na tupla
print(filmesTrupla.index("Pulp Fiction"))  # Retorna o índice do item na tupla
# print(filmesTrupla[0] = "Matrix")  # Erro! Tupla é imutável