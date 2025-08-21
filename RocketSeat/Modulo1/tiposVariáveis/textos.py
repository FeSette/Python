# Declaração

nomeCompleto = "Felipe Sette"

nomeCompletoAspas = """Felipe Sette"""

nomeCompletoQuebra = "Gabriel \
Casemiro"

nome = "Gabriel"
sobrenome = "Casemiro"

# Formação

print("Nome completo (1a forma):", nomeCompleto)
print("Nome completo (2a forma):" + nomeCompleto)
print("Nome completo (3a forma):" + "Felipe" + "Sette")
print("Nome completo (4a forma):" + "Felipe", "Sette")
print("Nome completo (5a forma):", nomeCompletoAspas)
print("Nome completo (6a forma):", nomeCompletoQuebra)
print("Nome completo (7a forma): %s" % nomeCompleto)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(sobrenome, nome))