import unittest
from book011_004_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testendo a classe AnonymousSurvey"""

    def setUp(self):
        """
        Cria a instancia de Survey e as variaveis que serão usadas no teste, essa funcao é executada antes dos testes
        e as variaveis criadas aqui são disponiveis nos testes
        """
        question = 'Qual a primeira lingua que você aprendeu?'
        self.minha_pesquisa = AnonymousSurvey(question)
        self.responses = ['English', 'Portuguese', 'Mandarin']

    def test_store_single_response(self):
        """Testando se apenas uma resposta é armazenada corretamente"""
        self.minha_pesquisa.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.minha_pesquisa.responses)

    def test_store_three_responses(self):
        """Testando se tres respostas são armazenadas corretamente"""
        for response in self.responses:
            self.minha_pesquisa.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.minha_pesquisa.responses)

unittest.main()
