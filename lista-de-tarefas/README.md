# 📋 Lista de Tarefas (Web + Python)

Uma aplicação web simples de Lista de Tarefas (*To-Do List*) construída para quem está começando a aprender desenvolvimento de software. O projeto demonstra de forma prática como o **Front-end** (HTML e CSS) conversa com o **Back-end** (Python com Flask) e salva informações em disco (`JSON`).

---

## ✨ Funcionalidades

- **Adicionar tarefas:** Digite uma nova atividade e salve-a na lista.
- **Concluir e Reabrir tarefas:** Alterne o status de uma tarefa entre **⏳ Pendente** e **✔ Concluída** com diferenciação visual clara (cores, etiquetas e texto riscado).
- **Remover tarefas:** Exclua atividades que não são mais necessárias.
- **Persistência de dados:** Todas as tarefas ficam salvas no arquivo `tarefas.json`, permanecendo guardadas mesmo após fechar o navegador ou desligar o computador.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Papel no Projeto |
| :--- | :--- | :--- |
| **Estrutura (Front-end)** | **HTML5** | Define os elementos da tela (formulário, botões e lista). |
| **Estilo (Front-end)** | **CSS3** | Define cores, alinhamentos e o visual diferente entre tarefas pendentes e concluídas. |
| **Servidor (Back-end)** | **Python + Flask** | Recebe os cliques do usuário, processa as regras e atualiza a página. |
| **Armazenamento** | **JSON** | Guarda a lista de tarefas em um arquivo de texto estruturado no computador. |

---

## 📂 Estrutura do Projeto

```text
lista-de-tarefas/
│
├── app.py               # Servidor Python (rotas e lógica de ler/salvar tarefas)
├── tarefas.json         # Arquivo onde as tarefas ficam guardadas no disco
├── test_app.py          # Testes automatizados da aplicação
├── requirements.txt     # Lista de bibliotecas Python necessárias
├── README.md            # Documentação do projeto
│
├── templates/           # Pasta padrão do Flask para arquivos HTML
│   └── index.html       # Estrutura visual da página
│
└── static/              # Pasta padrão do Flask para arquivos de estilo (CSS)
    └── style.css        # Aparência e cores da página
```

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado no computador.

### 2. Instalar as dependências
No terminal, instale o **Flask** executando:

```powershell
pip install -r requirements.txt
```
*(Ou diretamente `pip install flask`)*

### 3. Iniciar o servidor
Execute o arquivo principal do Python:

```powershell
python app.py
```

### 4. Acessar no navegador
Abra o seu navegador e acesse:
👉 **http://127.0.0.1:8080**

---

## 🧪 Como Executar os Testes Automatizados

O projeto conta com testes automatizados (usando a biblioteca `unittest` do Python) que verificam as funções de adicionar, concluir, reabrir e remover tarefas sem alterar o seu arquivo `tarefas.json` real.

Para rodar os testes, execute no terminal:

```powershell
python test_app.py
```
