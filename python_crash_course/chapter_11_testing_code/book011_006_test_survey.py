import unittest
from book011_004_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testendo a classe AnonymousSurvey"""

    def test_store_single_response(self):
        """Testando se apenas uma resposta é armazenada corretamente"""

        question = 'Qual a primeira lingua que você aprendeu?'
        minha_pesquisa = AnonymousSurvey(question)
        minha_pesquisa.store_response('English')

        self.assertIn('English', minha_pesquisa.responses)

    def test_store_three_responses(self):
        """Testando se tres respostas são armazenadas corretamente"""

        question = 'Qual a primeira lingua que você aprendeu?'
        minha_pesquisa = AnonymousSurvey(question)
        responses = ['English', 'Portuguese', 'Mandarin']
        for response in responses:
            minha_pesquisa.store_response(response)

        for response in responses:
            self.assertIn(response, minha_pesquisa.responses)

unittest.main()
