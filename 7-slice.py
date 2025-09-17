movieName = "Top Gum"

# string[inicio:fim] - inicio -> incluse | fim -> exclusive | indice começa em 0 | indice final -1

"""
string[inicio:fim:passo]
inicio -> incluse | fim -> exclusive
passo - determina o incremento. Padrão 1.
"""

# 1 - Buscar toda a string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda a string até a ultima posição
print(movieName[:7])

# 3 - Buscar toda a string da terceira posição até a ultima posição
print(movieName[2:])

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string dos nos índices impares
print(movieName[1::2])

# 6 - Inverter a string
print(movieName[::-1])