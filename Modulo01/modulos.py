print("Exemplo de importação de um módulo padrão:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A Raiz quadrada de 25 é {raiz_quadrada}")

# Exemplo de criação de módulo
print("\nExemplo de criação e utilização de módulo personalizado")
# from meu_modulo import saudacao, dobro
import meu_modulo
mensagem = meu_modulo.saudacao("Felipe")
resultado_dobro = meu_modulo.dobro(5)

print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")