# Declaração
minhaLista = [1, 2, 3, 4, 5, "lista", True, False]

# Exibindo a lista
print(f"minha lista de exemplo: {minhaLista}")

# Exibindo 
print(f"Meu elemento de índice 5 da minha lista: {minhaLista[5]}")
print(f"Meus elemento de índice 3 ao 7 da minha lista: {minhaLista[3:7]}")
print(f"Meu elemento de índice do 0 ao 6 da minha lista: {minhaLista[:6]}")
print(f"Meu elemento de índice do 0 ao 6 da minha lista: {minhaLista[2:]}")

# Alterando um elemento da minha lista
minhaLista[0] = "Python"
print(f"minha lista de exemplo: {minhaLista}")

## Métodos de lista
# append() - Adiciona um elemento no final da lista
minhaLista.append(6)
print(f"Lista após usar o método append: {minhaLista}")

# index() - Retorna o indice do elemento desejado
indice = minhaLista.index("lista")
print(f"O indice do elemento `lista` é: {indice}")

# insert() - Insere um elemento em um índice específico
minhaLista.insert(2, 10)
print(f"Índice 2, que era 3, agora é 10!: {minhaLista}")

# pop() - Remove e retorna o elemento de um índice específico
elementoRemovido = minhaLista.pop(3)
print(f"Elemento removido foi: {elementoRemovido}")
print(f"Minha lista após o pop(3): {minhaLista}")

# remove() - Remove o primeiro elemento informado
minhaLista.remove(True)
print(f"Minha lista após o elemento 'True' ser removido: {minhaLista}")

# sort() - ORganiza a lista em ordem 
lista = [3, 5, 2, 4, 1, 6, 8, 7]
lista.sort()
print(f"Minha lista após o método sort(): {lista}")