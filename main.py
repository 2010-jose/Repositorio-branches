def exibir_menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Sair")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada com sucesso!")
        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\nSua lista de tarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
