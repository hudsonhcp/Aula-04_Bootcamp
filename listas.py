#%%

produto: str = "sapato"
produto2: str = "camiseta"
produto3: str = "videogame"

produtos: list = []

produtos.append(produto)
produtos.append(produto2)
produtos.append(produto3)

produtos

#%%

# pop() sem argumento, retira o último item appendado da lista

produtos.pop(0)
produtos

#%%

lista = []

lista.extend(int(input("Digite um númedo: ")) for i in range(0,5))

lista

#%%

lista = []

lista.extend(range(1,10)) # Adiciona um argumento iterável

lista

lista_2 = lista.copy()

#%%

lista.pop()

print(lista)

print(lista_2)

#%%

lista_2 = lista

print(lista)

print(lista_2)

#%%

lista.pop(3)

print(lista)

print(lista_2)

#%%

lista_2.pop(0)

print(lista)

print(lista_2)

#%%

emails_list = [
    "ana.silva@gmail.com", "joao.pereira@outlook.com", "maria.oliveira@uol.com.br",
    "carlos.santos@yahoo.com", "ana.silva@gmail.com", "beatriz.souza@hotmail.com",
    "fernando.costa@icloud.com", "lucas.martins@gmail.com", "julia.almeida@live.com",
    "roberto.nunes@empresa.com.br", "maria.oliveira@uol.com.br", "paulo.ricardo@gmail.com",
    "camila.rocha@yahoo.com", "diego.lopes@outlook.com", "fernanda.lima@gmail.com",
    "gabriel.duarte@hotmail.com", "helena.vieira@uol.com.br", "igor.mendes@gmail.com",
    "joana.marques@outlook.com", "kevin.silva@yahoo.com", "larissa.gomes@gmail.com",
    "marcos.vinicius@live.com", "natalia.pinto@gmail.com", "otavio.augusto@empresa.com.br",
    "paula.fernandes@uol.com.br", "quenia.lopes@gmail.com", "rafael.soares@outlook.com",
    "sabrina.paiva@yahoo.com", "tiago.souza@gmail.com", "ursula.andrade@hotmail.com",
    "victor.hugo@icloud.com", "wagner.moura@gmail.com", "yasmin.lima@uol.com.br",
    "zeca.pagodinho@gmail.com", "ana.silva@gmail.com", "bruno.alves@outlook.com",
    "carla.diaz@yahoo.com", "daniel.farias@gmail.com", "eliane.rodrigues@live.com",
    "felipe.neto@empresa.com.br", "giovana.antonelli@uol.com.br", "hugo.gloss@gmail.com",
    "isabela.freitas@outlook.com", "joao.pereira@outlook.com", "karina.bacchi@yahoo.com",
    "leonardo.dicaprio@gmail.com", "marina.ruy@hotmail.com", "nicolas.prattes@icloud.com",
    "olivia.palermo@gmail.com", "pedro.sampaio@uol.com.br"
]

emails_unico = []
emails_duplicado = []

for _ in emails_list:
    if _ in emails_unico:
        emails_duplicado.append(_)
    else:
        emails_unico.append(_)

print(f"Emails únicos: {emails_unico}.")
print(f"Emails duplicados: {emails_duplicado}.")