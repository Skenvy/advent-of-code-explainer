from importlib import import_module
import os

YEAR_MODULE = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]

for day in range(1, 26):
    try:
        import_module(f'.day_{day}', package=f'advent_of_code_explainer.puzzles.{YEAR_MODULE}')
    except ModuleNotFoundError:
        pass
