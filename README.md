<div align="center">

# ✅ Gerenciador de Tarefas — Projeto em Python

</div>

---

## 🧾 **Resumo do Projeto**

Este projeto consiste em um **Gerenciador de Tarefas Pessoais** desenvolvido em **Python**, com o objetivo de aplicar os conceitos do **TDD (Test-Driven Development)** — Desenvolvimento Orientado por Testes.  

A ideia principal é construir um sistema simples e funcional de gerenciamento de tarefas, garantindo que cada funcionalidade seja implementada apenas após o sucesso dos testes automatizados.

---

## 🎯 **Objetivo**

O sistema foi criado para **organizar tarefas pessoais**, permitindo ao usuário:
- Criar tarefas com título e descrição.  
- Listar todas as tarefas cadastradas.  
- Marcar tarefas como **concluídas**.  
- Remover tarefas da lista.  
- Impedir o cadastro de tarefas com **título duplicado** ou **sem título**.

Além disso, o projeto demonstra **boas práticas de programação**, como:
- Escrita de código limpo e modular.  
- Separação entre regras de negócio e dados.  
- Uso de testes automatizados com **pytest**.  

---

## 🔄 **Metodologia — Ciclo TDD**

O desenvolvimento seguiu o ciclo clássico do **TDD**:

| Etapa | Nome | Descrição |
|:------|:------|:-----------|
| 🔴 RED | Escreve-se um **teste que falha propositalmente** antes da implementação. |
| 🟢 GREEN | Implementa-se o **código mínimo necessário** para o teste passar. |
| 🧼 REFACTOR | Refatora-se o código, mantendo todos os testes passando. |

Este método garante **qualidade, confiabilidade e clareza** no desenvolvimento do sistema.

---

## 🧩 **Estrutura do Projeto**

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
