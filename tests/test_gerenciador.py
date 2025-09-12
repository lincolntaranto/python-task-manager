import pytest

from src.gerenciador import GerenciadorDeTarefas

def test_adicionar_uma_tarefa_deve_aumentar_a_lista():
    gerenciador_teste = GerenciadorDeTarefas("data/test_tasks.json")
    gerenciador_teste.tarefas = []

    gerenciador_teste.adicionar_tarefa("Comprar pão")

    assert len(gerenciador_teste.tarefas) == 1
    assert gerenciador_teste.tarefas[0]["descricao"] == "Comprar pão"
    assert gerenciador_teste.tarefas[0]["status"] == "Pendente"

def test_marcar_tarefa_existente_deve_mudar_status_para_concluida():
    gerenciador_teste = GerenciadorDeTarefas("data/test_tasks.json")
    gerenciador_teste.tarefas = [{"descricao" : "Treinar Pytest", "status" : "Pendente"}]

    sucesso = gerenciador_teste.marcar_tarefa(0)

    assert sucesso is True
    assert gerenciador_teste.tarefas[0]["status"] == "Concluída"

def test_marcar_tarefa_existente_deve_mudar_status_para_pendente():
    gerenciador_teste = GerenciadorDeTarefas("data/test_tasks.json")
    gerenciador_teste.tarefas = [{"descricao" : "Treinar Pytest", "status" : "Concluída"}]

    sucesso = gerenciador_teste.marcar_tarefa(0)

    assert sucesso is True
    assert gerenciador_teste.tarefas[0]["status"] == "Pendente"

def test_marcar_tarefa_com_id_invalido():
    gerenciador_teste = GerenciadorDeTarefas("data/test_tasks.json")
    gerenciador_teste.tarefas = [{"descricao" : "Treinar Pytest", "status" : "Pendente"}]

    sucesso = gerenciador_teste.marcar_tarefa(1)

    assert sucesso is False

def test_salvar_tarefa():
    gerenciador_teste = GerenciadorDeTarefas("data/test_tasks.json")
    sucesso = gerenciador_teste.salvar_tarefas()

    assert sucesso is True

def test_carregar_tarefa():
    gerenciador_teste = GerenciadorDeTarefas("data/test_carregamento.json")
    sucesso = gerenciador_teste.carregar_tarefas()

    assert sucesso == []