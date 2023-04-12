# Sistema de perguntas e respostas

import random
import os

questions = [
    {
        'Pergunta': 'Quanto é 3+2?',
        'Opções': ['1','5','6','7'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 5*2?',
        'Opções': ['10','7','2.5','20'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 3*11?',
        'Opções': ['30','27','33','15'],
        'Resposta': '33',
    },
    {
        'Pergunta': 'Quanto é 4*5?',
        'Opções': ['16','20','22','10'],
        'Resposta': '20',
    },
]

decision = 's'
wrong_questions = 0
number_questions = 0
choice_int = None
right_answer = 0
index_question = random.randint(0,3)

while decision == 's':
    
    print(questions[index_question]['Pergunta'])

    options = questions[index_question]['Opções']
    for i,option in enumerate(options):
        print(f'{i})',option)

    choice = input('Qual a resposta certa? \n')


    if choice.isdigit():
        choice_int = int(choice)

    qtd_options = len(options)

    if choice_int is not None:
        if choice_int >= 0 and choice_int <qtd_options:
            if options[choice_int] == questions[index_question]['Resposta']:
                number_questions = number_questions + 1
                right_answer = right_answer + 1
            else:
                number_questions = number_questions + 1
                wrong_questions = wrong_questions + 1
    
    decision = input('Deseja continuar?  S/N\n').lower()
    os.system("cls")
print(f'Você acertou {number_questions - wrong_questions} perguntas!')