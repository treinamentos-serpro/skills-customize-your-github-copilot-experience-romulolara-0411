# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI, modelos Pydantic e operações CRUD. Pratique criação de rotas, validação de dados e respostas HTTP enquanto explora a documentação interativa da API.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota

#### Descrição
Use o código inicial para criar e executar uma aplicação FastAPI. Implemente uma rota de verificação de saúde e confira a documentação interativa gerada pelo framework.

Para preparar o ambiente, instale as dependências e salve o arquivo inicial como `main.py`:

```bash
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

#### Requisitos
O programa concluído deve:

- Criar uma rota `GET /health` que retorne o JSON `{"status": "ok"}`.
- Iniciar localmente com o comando `uvicorn main:app --reload`.
- Exibir a rota em `http://127.0.0.1:8000/docs`.

### 🛠️ Criar e Listar Tarefas

#### Descrição
Implemente as rotas para criar tarefas e listar todas as tarefas. Use os modelos Pydantic do código inicial para validar os dados recebidos e armazene os registros em memória.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para retornar a lista de tarefas.
- Implementar `POST /tasks` para criar uma tarefa com título, descrição e estado de conclusão.
- Atribuir um identificador único a cada tarefa criada e incluí-lo na resposta.
- Retornar `201 Created` quando uma tarefa for criada com sucesso.

### 🛠️ Consultar, Atualizar e Remover Tarefas

#### Descrição
Complete a API com operações para consultar, atualizar e remover uma tarefa pelo identificador. Use os códigos de status HTTP apropriados para indicar sucesso ou uma tarefa inexistente.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa e retornar `204 No Content`.
- Retornar `404 Not Found` quando o identificador não corresponder a uma tarefa.
- Permitir testar todas as rotas pela documentação em `/docs`.
