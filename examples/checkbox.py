# -*- coding: utf-8 -*-
"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""
import add_to_path
from pprint import pprint
from inquirer2 import prompt, Separator

from style import custom_style_2


questions = [
    {
        'type': 'checkbox',
        'qmark': '?',
        'message': 'Select toppings',
        'name': 'toppings',
        'choices': [
            Separator('= The Meats ='),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= The Cheeses ='),
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            Separator('= The usual ='),
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt.prompt(questions, style=custom_style_2)
pprint(answers)
