# -*- coding: utf-8 -*-
"""
When example
"""
import add_to_path
from inquirer2 import prompt, print_json

from style import custom_style_2


def dislikes_bacon(a):
    # demonstrate use of a function... here a lambda function would be enough
    return not a['bacon']


questions = [
    {
        'type': 'confirm',
        'name': 'bacon',
        'message': 'Do you like bacon?'
    },
    {
        'type': 'input',
        'name': 'favorite',
        'message': 'Bacon lover, what is your favorite type of bacon?',
        'when': lambda a: a['bacon']
    },
    {
        'type': 'confirm',
        'name': 'pizza',
        'message': 'Ok... Do you like pizza?',
        'default': False,  # only for demo :)
        'when': dislikes_bacon
    },
    {
        'type': 'input',
        'name': 'favorite',
        'message': 'Whew! What is your favorite type of pizza?',
        'when': lambda a: a.get('pizza', False)
    }
]

answers = prompt.prompt(questions, style=custom_style_2)

print_json(answers)
