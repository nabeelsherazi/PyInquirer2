# -*- coding: utf-8 -*-
"""
* example for rawlist question type
* run example by typing `python example/rawlist.py` in your console
"""
import add_to_path
from inquirer2 import prompt, print_json, Separator
from style import custom_style_2

questions = [{
    'type':
    'rawlist',
    'name':
    'theme',
    'message':
    'What do you want to do?',
    'choices': [
        'Order a pizza', 'Make a reservation',
        Separator(), 'Ask opening hours', 'Talk to the receptionist'
    ]
}, {
    'type':
    'rawlist',
    'name':
    'size',
    'message':
    'What size do you need',
    'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
    'filter':
    lambda val: val.lower()
}]

answers = prompt.prompt(questions, style=custom_style_2)
print_json(answers)
