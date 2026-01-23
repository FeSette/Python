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