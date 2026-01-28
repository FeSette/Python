# if, elif, else

idade = int(input("Quantos anos você tem?: "))

if idade >= 18:
    print("Você é maior de idade!")
elif idade >= 12:
    print("Você é um adolescente!")
else:
    print("você é menor de idade!")

# if, else na mesma linha
mensagem = "Você pode tirar a carteira de habilitação!" if idade>=18 else "você não pode tirar a carteira de habilitação!"
print(mensagem)