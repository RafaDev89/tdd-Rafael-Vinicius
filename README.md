# 🧠 Gerenciador de Tarefas — Test-Driven Development (TDD)

Este projeto implementa um **Gerenciador de Tarefas Pessoais** em **Python**, desenvolvido seguindo o método **TDD (Test-Driven Development)**, ou seja:

> **RED → GREEN → REFACTOR**

O objetivo é demonstrar o processo completo de criação de um sistema simples e testável, evoluindo o código apenas quando um teste falhar.

---

## 📋 Funcionalidades

O sistema permite:
- ✅ Criar tarefas com **título** e **descrição**  
- 📋 Listar todas as tarefas  
- ✔️ Marcar uma tarefa como concluída  
- ❌ Remover tarefas  
- 🚫 Impedir o cadastro de tarefas com **título duplicado** ou **sem título**

---

## 🧩 Estrutura do Projeto

gerenciador_tarefas/
│
├── tarefa.py # Classe Tarefa
├── gerenciador.py # Classe GerenciadorTarefas
└── test_gerenciador.py # Testes automatizados (pytest)


---

## ⚙️ Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [pytest](https://docs.pytest.org/en/stable/)

Instale o pytest com:

pip install pytest

🧪 Executando os testes

Abra o terminal na pasta do projeto:

cd caminho/para/gerenciador_tarefas

Execute o pytest:

pytest -v


O pytest exibirá o resultado de cada teste, por exemplo:

=========================== test session starts ============================
collected 3 items

test_gerenciador.py::test_adicionar_tarefa PASSED
test_gerenciador.py::test_nao_permite_titulo_vazio_ou_duplicado PASSED
test_gerenciador.py::test_concluir_e_remover_tarefa PASSED

============================ 3 passed in 0.10s =============================

🔄 Ciclo TDD utilizado

RED → Escreva um teste que falha.
Exemplo: test_gerenciador.py tenta usar uma classe que ainda não existe.

GREEN → Implemente o código mínimo necessário para o teste passar.
Exemplo: criar gerenciador.py com uma classe simples GerenciadorTarefas.

REFACTOR → Melhore o código mantendo todos os testes passando.
Exemplo: criar a classe Tarefa separada e validar títulos duplicados.

✅ Comandos úteis

Rodar apenas um teste específico:

pytest -v -k test_adicionar_tarefa


Ver relatório de cobertura (opcional):

pip install pytest-cov
pytest --cov=.


Limpar arquivos de cache do pytest:

pytest --cache-clear


👨‍💻 Autor

Rafael Vinícius
Desenvolvido como parte de um exercício de TDD em Python.
