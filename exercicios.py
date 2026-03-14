#%%
## Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros: dict = {}

cont = 1

while True:

    titulo = input("Título do livro: ")
    autor = input("Autor dp livro: ")
    ano = input("Ano do livro: ")

    livros[f"livro_{cont}"] = {"titulo": titulo,
                                   "autor": autor,
                                   "ano": ano}
    
    cont += 1

    continuar = input("Quer continuar [s/n]: ").lower()[0]

    if continuar == "s":
        pass
    else:
        print("Ok, vamos parar e listar os livros...")
        break

for c, v in livros.items():
    for i, j in v.items():
        print(i, ": ", j)
    print("-----")