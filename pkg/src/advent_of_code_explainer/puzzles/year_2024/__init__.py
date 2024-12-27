from datetime import datetime, UTC
from importlib import import_module
import os

CURRENT_TIME = datetime.now(UTC)
YEAR_MODULE = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]

for day in range(1, CURRENT_TIME.day+1):
    try:
        import_module(f'.day_{day}', package=f'advent_of_code_explainer.puzzles.{YEAR_MODULE}')
    except ModuleNotFoundError:
        pass
