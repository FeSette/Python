## Tupla é uma lista de elementos IMUTÁVEIS (Não pode remover, inserir 
# e alterar)

minhaTupla = (1, 2, 2, 3, 2, 4, 5)
print(f"Minha tupla: {minhaTupla}")

# Acessar elementos
print(f"Meu elemento de índice 1: {minhaTupla[1]}")
print(f"Meu elemento de índice 3: {minhaTupla[3]}")

# Acessar o último elemento
print(f"Meu último elemento da minha tupla: {minhaTupla[-1]}")

## Métodos
# count - Conta quantas vezes o elemento informado aparece na tupla
contagem = minhaTupla.count(2)
print(f"Quantidade de vezes que o elemento 2 aparece: {contagem}")

# index - mostra o primeiro indice do elemento informado
indice = minhaTupla.index(4)
print(f"Indice da primeira ocorrência do elemento 4: {indice}")
