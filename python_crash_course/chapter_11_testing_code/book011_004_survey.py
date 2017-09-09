class AnonymousSurvey():
    """Coleção de respostas anonimas para uma pesquisa de uma pergunta"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("Resultados da pesquisa:")
        for response in self.responses:
            print('-', response)