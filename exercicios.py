#%%

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista = [i for i in range(1, 11)]

for l in lista:
    print(f"- {l}**2 = {l**2}.", end = "\n")

#%%

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista = ["Python", "Java", "C++", "JavaScript"]

lista.remove("C++")
lista.append("Ruby")
lista

#%%
## 03. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

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
    print(c)
    print("-----")
    for i, j in v.items():
        
        print(i, ": ", j)
    print("-=-=-=-=-=-=")


# %%
# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

palavra = 'O rato roeu a roupa do rei de roma.'
dicionario = {}
for p in palavra:
    if p not in dicionario.keys():
        dicionario[f'{p}'] = palavra.count(p)
    else:
        pass

for k, v in dicionario.items():
    if v > 1:
        print(f"{k}: {v} vezes.")
    else:
        print(f"{k}: {v} vez.")

#%%
# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
dicionário = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = 0

for l in lista:
    preco_total += dicionário[l]

print(f"O preço total foi de R$ {preco_total:.2f}.")

#%%
# 6. Eliminação de Duplicatas
#Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]


emails_unicos = list(set(emails))
# Set em uma lista retorna apenas os ítens únicos, retirando duplicações.

print(emails_unicos)

#%%

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

import random

lista = [random.randint(1, 100) for i in range (100)]

print("Apenas essas idades são menores que 18 anos: ")
for l in lista:
    if l < 18:
        print(l)
    else:
        pass

#%%
# 8. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}]

pessoas.sort(key = lambda pessoa: pessoa["nome"])

print(pessoas)

#%%
# 9. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.

lista = [random.randint(1, 100) for i in range(100)]

soma = 0

for l in lista:
    soma += l

media = soma/len(lista)

print(f"A média desses {len(lista)} números é {media:.2f}.")

#%%
# 10. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

lista = [random.randint(1,100) for i in range(100)]

lista_pares = [p for p in lista if p % 2 == 0]
lista_impares = [i for i in lista if i % 2 != 0]

print(f"Essa é a lista com os {len(lista_pares)} números pares: {lista_pares}.")
print(f"Essa é a lista com os {len(lista_impares)} os números ímpares: {lista_impares}.")

#%%
# 11. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90

for i in produtos:
    if i["id"] == 2:
        i["preço"] = 90

produtos[1]

#%%
# 12. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario = {}
for k, v in dicionario1.items():
    dicionario[f'{k}'] = v
for k, v in dicionario2.items():
    dicionario[f'{k}'] = v

print(dicionario)

#dicionario_fundido = {**dicionario1, **dicionario2}

#print(dicionario_fundido)

#%%
# 13. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

filtrados = {}

for k, v in estoque.items():
    if v > 0:
        filtrados[f"{k}"] = v
    else:
        pass

print(filtrados)

#%%
# 14. Extração de Chaves e Valores
#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}

chaves = []
valores = []

for k, v in dicionario.items():
    chaves.append(k)
    valores.append(v)

# chaves = list(dicionario.keys())
# valores = list(dicionario.values())

print(f"chaves: {chaves}.")
print(f"valores: {valores}.")

