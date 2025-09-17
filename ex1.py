# Exercicio 1 - Concatenação de strings

nome = input("Digite o nome:\n")
sobrenome = input("Digite o sobrenome:\n")

nomeCompleto = f"{sobrenome}, {nome}"
print(nomeCompleto)

#Exercicio 2 - Inversão de strings num texto

texto = "Python é muito interessante"

palavras = texto.split(" ")
palavrasInvertidas = palavras[::-1]
textoInvertido = " ".join(palavrasInvertidas)
print(textoInvertido)

# Exercicio 3 - Verificação se o testo é palíndromo

texto1 = "arara"
texto2 = "python"

texto1_normalizado = texto1.replace(" ", "").lower()
texto2_normalizado = texto2.replace(" ", "").lower()

palindromo1 = texto1_normalizado == texto1_normalizado[::-1]
palindromo2 = texto2_normalizado == texto2_normalizado[::-1]

print(f"O texto '{texto1}' é um palíndromo? {palindromo1}")
print(f"O texto '{texto2}' é um palíndromo? {palindromo2}")
