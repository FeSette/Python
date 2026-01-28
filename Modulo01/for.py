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

# range() - Intervalo numérico
for numero in range(5):
    print(f"Numero: {numero}")

# range() com len()
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 1
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
