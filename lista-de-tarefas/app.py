from flask import Flask, render_template, request, redirect, url_for
import json
import os

# Cria a nossa aplicação web com Flask
app = Flask(__name__)

# Nome do arquivo onde vamos guardar as tarefas
ARQUIVO_TAREFAS = os.path.join(os.path.dirname(__file__), 'tarefas.json')


# ==========================================
# FUNÇÕES AUXILIARES (Ler e Salvar no Disco)
# ==========================================

def carregar_tarefas():
    """Lê a lista de tarefas salva no arquivo tarefas.json."""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def salvar_tarefas(tarefas):
    """Guarda a lista de tarefas atualizada dentro do arquivo tarefas.json."""
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


# ==========================================
# ROTAS DA APLICAÇÃO (Caminhos do Site)
# ==========================================

@app.route('/')
def index():
    """Página principal: carrega as tarefas e mostra o HTML na tela."""
    tarefas = carregar_tarefas()
    return render_template('index.html', tarefas=tarefas)


@app.route('/adicionar', methods=['POST'])
def adicionar():
    """Recebe o texto do formulário HTML e cria uma nova tarefa."""
    texto_tarefa = request.form.get('texto_tarefa', '').strip()

    if texto_tarefa:
        tarefas = carregar_tarefas()

        # Gera um ID único simples (pega o maior ID atual e soma 1)
        novo_id = max([t['id'] for t in tarefas], default=0) + 1

        nova_tarefa = {
            'id': novo_id,
            'texto': texto_tarefa,
            'concluida': False
        }

        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)

    # Redireciona de volta para a página principal
    return redirect(url_for('index'))


@app.route('/concluir/<int:id_tarefa>', methods=['POST'])
def concluir(id_tarefa):
    """Alterna o estado da tarefa entre concluída (True) e pendente (False)."""
    tarefas = carregar_tarefas()

    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['concluida'] = not tarefa['concluida']
            break

    salvar_tarefas(tarefas)
    return redirect(url_for('index'))


@app.route('/remover/<int:id_tarefa>', methods=['POST'])
def remover(id_tarefa):
    """Remove uma tarefa da lista pelo seu ID."""
    tarefas = carregar_tarefas()

    # Filtra a lista mantendo apenas as tarefas com ID diferente do que queremos apagar
    tarefas = [t for t in tarefas if t['id'] != id_tarefa]

    salvar_tarefas(tarefas)
    return redirect(url_for('index'))


# Inicia o servidor quando executamos "python app.py"
# Usamos a porta 8080 pois a porta padrão (5000) às vezes é bloqueada pelo Windows
if __name__ == '__main__':
    app.run(debug=True, port=8080)

