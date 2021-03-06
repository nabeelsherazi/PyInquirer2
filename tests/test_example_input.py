# -*- coding: utf-8 -*-
import textwrap
import pdb
import time

from .helpers import keys
from .helpers import create_example_fixture

example_app = create_example_fixture('examples/input.py')


def test_input(example_app):
    example_app.expect(
        textwrap.dedent("""\
        ? What's your first name"""))

    example_app.writeline('John')

    # In the next question, "Doe" will be the default answer

    example_app.expect(
        textwrap.dedent("""\
        ? What's your first name  John
        ? What's your last name  Doe"""))

    example_app.write(keys.ENTER)

    example_app.expect(
        textwrap.dedent("""\
        ? What's your last name  Doe
        ? What's your phone number"""))

    example_app.writeline('0123456789')
    example_app.expect(
        textwrap.dedent("""\
        ? What's your phone number  0123456789
        {'first_name': 'John', 'last_name': 'Doe', 'phone': '0123456789'}
        """))
