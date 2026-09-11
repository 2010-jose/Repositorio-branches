def exibir_menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")  # Nova opção adicionada
    print("4. Sair")             # Opção atualizada

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
        elif opcao == "3":  # Nova funcionalidade implementada
            if not tarefas:
                print("Não há tarefas para remover.")
            else:
                print("\nSua lista de tarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
                try:
                    indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                    if 0 <= indice < len(tarefas):
                        removida = tarefas.pop(indice)
                        print(f"Tarefa '{removida}' removida com sucesso!")
                    else:
                        print("Número de tarefa inválido.")
                except ValueError:
                    print("Por favor, digite um número válido.")
        elif opcao == "4":  # Opção de sair atualizada
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
