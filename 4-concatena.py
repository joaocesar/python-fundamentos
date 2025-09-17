name = input("Digite o nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("===============================")

# Alternativa 1
# print("Nome do Filme: ", name)
# print("Ano do Lançamento: ", yearLaunch)
# print("Nota do publico: ", noteMovie)

# Alternativa 2
# print("Nome do Filme:", name, "\nAno do Lançamento:", yearLaunch, "\nNota do publico:", noteMovie)

# Alternativa 3
print(f"Nome do Filme: {name}"
      f"\nAno do Lançamento: {yearLaunch}"
      f"\nNota do publico: {noteMovie}\n"
      )

