import pytest
from gerenciador import GerenciadorTarefas

def test_adicionar_tarefa():
    g = GerenciadorTarefas()
    g.adicionar_tarefa("Estudar Python", "Aprender TDD em Python")
    tarefas = g.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"
    assert tarefas[0]["descricao"] == "Aprender TDD em Python"
    assert tarefas[0]["status"] == "pendente"

def test_nao_permite_titulo_vazio_ou_duplicado():
    g = GerenciadorTarefas()
    g.adicionar_tarefa("Estudar", "Aprender TDD")

    with pytest.raises(ValueError):
        g.adicionar_tarefa("", "Sem título")

    with pytest.raises(ValueError):
        g.adicionar_tarefa("Estudar", "Duplicado")

