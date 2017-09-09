from book011_004_survey import AnonymousSurvey

question = 'Qual a primeira lingua que você aprendeu?'
minha_pesquisa = AnonymousSurvey(question)

minha_pesquisa.show_question()
print("Digite 'q' para sair")

while True:
    response = input('Lingua: ')
    if response == 'q':
        break

    minha_pesquisa.store_response(response)

print("\nObrigado por participar da pesquisa!")
minha_pesquisa.show_results()