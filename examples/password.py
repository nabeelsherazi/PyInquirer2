# -*- coding: utf-8 -*-
"""
* password question example
"""
import add_to_path
from inquirer2 import prompt, print_json
from style import custom_style_2

questions = [{
    'type': 'password',
    'message': 'Enter your git password',
    'name': 'password'
}]

answers = prompt.prompt(questions, style=custom_style_2)
print_json(answers)
