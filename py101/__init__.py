from story.story import BaseStory
from story.translation import gettext as _

from . import (introduction,)


__author__ = """Sophilabs"""
__email__ = 'hi@sophilabs.co'
__version__ = '0.4.10'


class Story(BaseStory):

    name = 'py101'
    title = _('Learn regular expressions with Python')
    adventures = [
        introduction
    ]
