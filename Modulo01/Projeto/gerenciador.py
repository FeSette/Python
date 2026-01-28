# Adicionar tarefa -----------------------
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")

# Ver tarefa ----------------------------
def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

# Atualizar tarefa ----------------------
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Índice de tarefa inválido!")
    return

# Completar tarefa -----------------------
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

tarefas = []
# Menu do programa -----------------------
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        nome_tarefa = input("Digite o nome da sua tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif opcao == "2":
        ver_tarefas(tarefas)    
    elif opcao == "3":
        ver_tarefas(tarefas)    
        indice_tarefa = input("Digite o número da tarefa a atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif opcao == "4":
        ver_tarefas(tarefas) 
        indice_tarefa = input("Digite o número da tarefa a completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif opcao == "6":
        break

print("Programa finalizado")