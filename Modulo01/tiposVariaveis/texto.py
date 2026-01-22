## Declaração
nomeCompleto = "Felipe Sette"
nome = "Felipe"
sobrenome = "Sette"

# Declaração com 3x aspas permite a quebra de linha na declaração e no resultado
nomeCompletoAspas = """Felipe
Sette"""

# Declaração com quebra de linha usando a \ na declaração, porém no resultado fica na mesma linha
nomeCompletoQuebra = "Felipe \
Sette"

## Formatação das variáveis
print("Nome completo (1a forma):", nomeCompleto)
print("Nome completo (2a forma):"+ nomeCompleto)
print("Nome completo (3a forma):"+ "Felipe"+"Sette")
print("Nome completo (4a forma):"+ "Felipe","Sette")
print("Nome completo (5a forma):", nomeCompletoAspas)
print("Nome completo (6a forma):", nomeCompletoQuebra)
print("Nome completo (7a forma): %s"% nomeCompleto)
print("Nome completo (8a forma): %s %s"% (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))

""" 
## Principais métodos do tipo texto

nome.upper() - mostra o texto da variável em MAIUSCULO
nome.lower() - mostra o texto da variável em MINUSCULO
nome[0] - Exibe apenas a primeira letra do texto da variável
nomeCompleto.count("e") - Vai contar quantas letras "e" tem na variável
nomeCompleto.find("e") - Vai informar o número da posição da primeira letra "e"
nome.encode() - Usado para converter uma String em Bytes usando codificação
nome.encode().decode() - Converter a codificação de Bytes em String
nomeCompleto.replace("b", "a") - Vai substituir a letra "b" pela letra "a"
nomeCompleto.replace("a", "b").replace("c", "d").replace("e", "f")
"-".join("Felipe") - Vai incluir o "-" entre cada caracter da string
nomeCompleto.split() - Vai dividir a string em lista = ['Felipe', 'Sette']

#Comparadores
nomeCompleto.startswith("Fe") - Vai verificar se a minha variável começa com "Fe" e retornar TRUE
"li" in nomeCompleto - Vai verificar se na variável tem "li" e vai retornar TRUE
"li" not in nomeCompleto - Vai verificar se "li" está presente na variável e retornar FALSE
"""