from .core import GerenciadorDeTarefas

def run():

    local_arquivo = "data/data.json"
    gerenciador = GerenciadorDeTarefas(local_arquivo)

    while True:
        print("""
            1. Adicionar Tarefa
            2. Listar Tarefas
            3. Definir Status da Tarefa
            4. Adicionar tarefa da API
            5. Sair""")
        try:
            escolha = int(input("Entrada: "))
            if escolha == 1:
                gerenciador.adicionar_tarefa(input("Informe a descricação: "))
            elif escolha == 2:
                gerenciador.listar_tarefas()
            elif escolha == 3:
                gerenciador.listar_tarefas()
                try:
                    print("Informe o ID da tarefa!")
                    id = int(input("Entrada: ")) - 1
                    gerenciador.marcar_tarefa(id)
                except ValueError:
                    print("Informe apenas números!")
            elif escolha == 4:
                api = gerenciador.buscar_tarefa_da_api()
                if api:
                    gerenciador.adicionar_tarefa(api)
                else:
                    print("Falha ao adicionar nova tarefa.")
            elif escolha == 5:
                print("Saindo...")
                break
            else:
                print("Escolha invalida!")
        except ValueError:
            print("Digite apenas números!")