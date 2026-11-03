import os
import json
import tempfile
import unittest
import app as aplicacao


class TesteListaDeTarefas(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste: cria um arquivo JSON temporário para não bagunçar suas tarefas reais."""
        self.arquivo_temp = tempfile.NamedTemporaryFile(delete=False, suffix='.json', mode='w', encoding='utf-8')
        json.dump([], self.arquivo_temp)
        self.arquivo_temp.close()

        # Aponta a aplicação para o arquivo temporário de testes
        aplicacao.ARQUIVO_TAREFAS = self.arquivo_temp.name
        aplicacao.app.config['TESTING'] = True
        self.cliente = aplicacao.app.test_client()

    def tearDown(self):
        """Executado depois de cada teste: apaga o arquivo temporário."""
        if os.path.exists(self.arquivo_temp.name):
            os.remove(self.arquivo_temp.name)

    def test_1_pagina_inicial_vazia(self):
        """Testa se a página abre corretamente quando não há tarefas."""
        resposta = self.cliente.get('/')
        self.assertEqual(resposta.status_code, 200)
        html = resposta.data.decode('utf-8')
        self.assertIn('Nenhuma tarefa por enquanto', html)

    def test_2_adicionar_tarefa_pendente(self):
        """Testa adicionar uma tarefa e verifica se aparece com visual de pendente."""
        resposta = self.cliente.post('/adicionar', data={'texto_tarefa': 'Estudar testes em Python'}, follow_redirects=True)
        self.assertEqual(resposta.status_code, 200)

        html = resposta.data.decode('utf-8')
        self.assertIn('Estudar testes em Python', html)
        self.assertIn('item-tarefa pendente', html)
        self.assertIn('⏳ Pendente', html)

        # Verifica se salvou no arquivo JSON
        tarefas = aplicacao.carregar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertFalse(tarefas[0]['concluida'])

    def test_3_concluir_e_reabrir_tarefa(self):
        """Testa marcar uma tarefa como concluída (mudança visual) e depois reabri-la."""
        # 1. Adiciona a tarefa
        self.cliente.post('/adicionar', data={'texto_tarefa': 'Fazer exercícios'})

        # 2. Marca como concluída (ID 1)
        resposta = self.cliente.post('/concluir/1', follow_redirects=True)
        html = resposta.data.decode('utf-8')

        # Verifica se mudou para o visual de concluída no HTML
        self.assertIn('item-tarefa concluida', html)
        self.assertIn('✔ Concluída', html)
        self.assertIn('↩️ Reabrir', html)

        # Verifica se salvou como True no JSON
        tarefas = aplicacao.carregar_tarefas()
        self.assertTrue(tarefas[0]['concluida'])

        # 3. Clica novamente para reabrir a tarefa
        resposta_reabrir = self.cliente.post('/concluir/1', follow_redirects=True)
        html_reabrir = resposta_reabrir.data.decode('utf-8')
        self.assertIn('item-tarefa pendente', html_reabrir)
        self.assertFalse(aplicacao.carregar_tarefas()[0]['concluida'])

    def test_4_remover_tarefa(self):
        """Testa excluir uma tarefa e verifica se ela some da tela e do JSON."""
        self.cliente.post('/adicionar', data={'texto_tarefa': 'Tarefa para apagar'})

        resposta = self.cliente.post('/remover/1', follow_redirects=True)
        html = resposta.data.decode('utf-8')

        self.assertNotIn('Tarefa para apagar', html)
        self.assertEqual(len(aplicacao.carregar_tarefas()), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
