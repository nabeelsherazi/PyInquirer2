# -*- coding: utf-8 -*-
"""
* Confirm question example
* run example by typing `python example/confirm.py` in your console
"""
import add_to_path
from pprint import pprint

from inquirer2 import prompt

from style import custom_style_1

questions = [
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    },
    {
        'type': 'confirm',
        'message': 'Do you want to exit?',
        'name': 'exit',
        'default': False,
    },
]

answers = prompt.prompt(questions, style=custom_style_1)
pprint(answers)
