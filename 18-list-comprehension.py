filmes = ["O Senhor dos Anéis", "Matrix", "Clube da Luta", "Pulp Fiction"]

filmesComALetraU = [filme for filme in filmes if "u" in filme.lower()]
print(filmesComALetraU)
print("-----------")
filmesComMaisDe10Letras = [filme for filme in filmes if len(filme) > 10]
print(filmesComMaisDe10Letras)
print("-----------")

while True:
    nomeDoFilme = input("Digite o nome do filme (ou 'sair' para encerrar): ")
    if nomeDoFilme.lower() == "sair": 
        print("Encerrando o programa.")
        break
    filmesEncontrados = [filme for filme in filmes if nomeDoFilme.lower() in filme.lower()]
    if filmesEncontrados:
        print(f"Filme(s) encontrado(s) com o nome {nomeDoFilme}:")
        for filme in filmesEncontrados:
            print(f"- {filme}")
    else:
        print(f"Nenhum filme encontrado com com o nome {nomeDoFilme}.")
print("-----------")
