#Declaração

# Dicionário Pessoa
pessoa = {"nome": "Felipe", "idade": 30, "cidade": "São Paulo"}
print(f"Meu dicionário: {pessoa}")

# Acessar valores por chave
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")

# Inserindo chave e valor
pessoa["sobrenome"] = "Sette"
print(f"Meu dicionário: {pessoa}")
print(f"Sobrenome: {pessoa['sobrenome']}")

## Métodos

# Alterar o valor de uma Key
pessoa["idade"] = 31
print(f"Idade atualizada: {pessoa['idade']}")

# Removendo um par chave-valor
del pessoa["sobrenome"]
print(f"Meu dicionário: {pessoa}")

# Keys()
# Tranformar o dicionário em uma lista
chaves = list(pessoa.keys())
print(f"Chaves do dicionário: {chaves}")
print(f"Primeira chave: {chaves[0]}")

# values()
valores = list(pessoa.values())
print(f"Valores do dicionário: {valores}")
print(f"Primeiro valor: {valores[0]}")

# items() - O resultado é uma tupla
itens = list(pessoa.items())
print(f"Pares chave-valor do dicionário: {itens}")
print(f"Primeira chave-valor: %s = %s" %(itens[0][0], itens[0][1]))