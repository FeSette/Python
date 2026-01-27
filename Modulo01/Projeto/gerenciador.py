# Adicionar tarefa -----------------------
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")

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
    if opcao == "6":
        break

print("Programa finalizado")