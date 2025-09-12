from gerenciador import GerenciadorDeTarefas

def main():
    local = "data/data.json"
    app = GerenciadorDeTarefas(local)
    app.executar()

if __name__ == "__main__":
    main()
