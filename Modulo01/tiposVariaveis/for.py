# Utilizando lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Utlizando tupla
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

# Utilizando dicionário
pessoa = {"nome": "Felipe", "idade": 32, "cidade": "São Paulo"}
for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")