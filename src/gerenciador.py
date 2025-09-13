import json
import random
import requests

class GerenciadorDeTarefas:
    def __init__(self, nome_arquivo):
        print(f"Lista criada! Nome do arquivo: {nome_arquivo}")
        self.nome_arquivo = nome_arquivo
        self.tarefas = self.carregar_tarefas()

    def adicionar_tarefa(self, descricao):

        """Adiciona uma nova tarefa a lista de tarefas.

        Args:
            descricao (str): Descricação da tarefa a ser adicionada.

        Returns:
            None.
        """

        self.tarefas.append({"descricao" : descricao, "status" : "Pendente"})
        print(f"Tarefa '{descricao}' criada com sucesso!")
        self.salvar_tarefas()

    def listar_tarefas(self):

        """Itera sobre a lista de dicionários "tarefas" do objeto.

        Args:
            None.

        Returns:
            None.
        """

        print("---Lista de Tarefas---")
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1} - {tarefa["descricao"]} : {tarefa["status"]}")
    
    def marcar_tarefa(self, id):

        """Itera sobre as tarefas existentes e caso exista ela tem o status atualizado
        caso não, ela informa que o ID não foi encontrado.

        Args:
            id (int): ID da tarefa a ser atualizada.

        Returns:
            bool: True caso encontre um ID valido e False caso não encontre.
        """

        for i, tarefa in enumerate(self.tarefas):
            if i == id:
                if tarefa["status"] == "Pendente":
                    tarefa["status"] = "Concluída"
                    print(f"Alterado o status da tarefa {tarefa["descricao"]} para concluída!")
                    self.salvar_tarefas()
                    return True
                else:
                    tarefa["status"] = "Pendente"
                    print(f"Alterado o status da tarefa {tarefa["descricao"]} para pendente!")
                    self.salvar_tarefas()
                    return True
        else:
            print("ID não encontrado!")
            return False

    def salvar_tarefas(self):

        """Salva a lista de tarefas em um arquivo json e retorna True em caso de sucesso e False em caso de falha.

        Args:
            None.

        Returns:
            bool: True em caso de sucesso e False em caso de falha.
        """

        try:
            with open(self.nome_arquivo, "w") as arquivo:
                json.dump(self.tarefas, arquivo, indent=4)
            print("Progresso salvo com sucesso!")
            return True
        except PermissionError:
            print("Problema de permissão! Falha ao salvar.")
            return False
    
    def carregar_tarefas(self):

        """Carrega a lista de dicionários contendo as tarefas e a retorna, em caso de falha retorna uma lista vazia.

        Args:
            None.

        Returns:
            list: Uma lista de dicionários representando as tarefas carregadas com sucesso, ou uma lista vazia caso ocorra alguma falha.
        """

        try:
            with open(self.nome_arquivo, "r") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print("Arquivo não encontrado! Iniciando uma nova lista vazia.")
            return []
    
    def adicionar_tarefa_da_api(self):

        """Gera um número aleatório, concatena com a URL da API, faz a requisição, verifica se a requisição foi bem sucedida, converte o 
        conteúdo para um dicionário python e então retorna o title.

        Args:
            None

        Returns:
            str: Retorna o título da tarefa obtido do dicionário retornado pela API.
            bool: Retorna False em caso de falha ao chamar a API.
        """

        numero_aleatorio = random.randint(1,100)
        url = f"https://jsonplaceholder.typicode.com/todos/{numero_aleatorio}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()
            return dados["title"]
        except requests.exceptions.RequestException as e:
            print(f"Erro ao chamar API: {e}")
            return False


    def executar(self):
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
                    self.adicionar_tarefa(input("Informe a descricação: "))
                elif escolha == 2:
                    self.listar_tarefas()
                elif escolha == 3:
                    self.listar_tarefas()
                    try:
                        print("Informe o ID da tarefa!")
                        id = int(input("Entrada: ")) - 1
                        self.marcar_tarefa(id)
                    except ValueError:
                        print("Informe apenas números!")
                elif escolha == 4:
                    api = self.adicionar_tarefa_da_api()
                    if api == False:
                        print("Falha ao adicionar nova tarefa.")
                    else:
                        self.adicionar_tarefa(api)
                elif escolha == 5:
                    print("Saindo...")
                    break
                else:
                    print("Escolha invalida!")
            except ValueError:
                print("Digite apenas números!")