# Exemplo de função
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudacao..")
saudacao("Any")
saudacao("Felipe")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado..")
resultado_quadrado = quadrado(5)
print(f"Resultado da função quadrado: {resultado_quadrado}")

# Função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma..")
resultado_soma = soma(20, 50)
print(f"A soma da função soma é: {resultado_soma}")