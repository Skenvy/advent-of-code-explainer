from datetime import datetime, UTC
from importlib import import_module
from sys import modules
from types import ModuleType


CURRENT_TIME = datetime.now(UTC)
MOST_RECENT_DECEMBER_YEAR = CURRENT_TIME.year if CURRENT_TIME.month == 12 else CURRENT_TIME.year - 1
PKG = 'advent_of_code_explainer.puzzles'

for year in range(2015, MOST_RECENT_DECEMBER_YEAR+1):
    try:
        import_module(f'.year_{year}', package=PKG)
    except ModuleNotFoundError:
        modules[f'{PKG}.year_{year}'] = ModuleType(f'{PKG}.year_{year}')
        for day in range(1, CURRENT_TIME.day+1 if year == MOST_RECENT_DECEMBER_YEAR else 26):
            modules[f'{PKG}.year_{year}.day_{day}'] = ModuleType(f'{PKG}.year_{year}.day_{day}')
            def solve_one(*args, **kwargs):
                raise NotImplementedError
            def solve_two(*args, **kwargs):
                raise NotImplementedError
            modules[f'{PKG}.year_{year}.day_{day}'].solve_one = solve_one
            modules[f'{PKG}.year_{year}.day_{day}'].solve_two = solve_two
        import_module(f'{PKG}.year_{year}')