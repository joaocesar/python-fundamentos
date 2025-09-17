movieName = "Top Gun"
movieName2 = 'top gun'
print(movieName == movieName2)  # False

movieDescription = """
Top Gun é um filme de ação americano de 1986 dirigido por Tony Scott, produzido por
Don Simpson e Jerry Bruckheimer, e estrelado por Tom Cruise como Pete "Maverick" Mitchell,
um jovem piloto de caça talentoso e destemido que é enviado para a escola de elite de pilotos
Top Gun na Califórnia.
"""

print(movieName)
print("=" * 100)
print(movieDescription)

# Multiplicação de strings

line = "="
print(line * 50)

# Procurar uma substring dentro de uma string: <sub> in <str>

print("Gun" in movieName)  # True
print("gun" in movieName)  # False
