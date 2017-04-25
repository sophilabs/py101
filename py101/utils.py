import importlib
import inspect
import random
import sys
import os

from story.adventures import AdventureVerificationError
from story.translation import gettext as _


def load_solution_function(file, parameters=1):
    try:
        path, file = os.path.split(os.path.abspath(file))
        sys.path.append(path)
        if file.endswith('.py'):
            module_name = file[:-3]
        elif file.endswith('.pyc'):
            module_name = file[:-4]
        else:
            module_name = file
        module = importlib.import_module(module_name)
        function = inspect.getmembers(module, inspect.isfunction)[0][1]
        assert len(inspect.signature(function).parameters) == parameters
        return function
    except ImportError:
        raise AdventureVerificationError(
            _('I can\'t import a module from {}. Are you sure the file exists '
              'and it\'s a valid python file?').format(file))
    except IndexError:
        raise AdventureVerificationError(
            _('I can\'t find a function definition in {}. Read the adventure '
              'again and use the template proposed there.').format(file))
    except AssertionError:
        raise AdventureVerificationError(
            _('I found a function in your file but it doesn\'t accept the '
              'required number of parameters ({}). If you define several '
              'functions in your file, make sure the solution function is the '
              'first one.'.format(parameters)))


def get_random_string(dictionary, min_length, max_length):
    result = ''
    length = random.randint(min_length, max_length)
    while len(result) < length:
        result += random.choice(dictionary)
    return result
