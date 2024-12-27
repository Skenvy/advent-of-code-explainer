# from datetime import datetime, UTC # only works python >= 3.11
from datetime import datetime, timezone
from importlib import import_module

# CURRENT_TIME = datetime.now(UTC) # only works python >= 3.11
CURRENT_TIME = datetime.now(timezone.utc)
MOST_RECENT_DECEMBER_YEAR = CURRENT_TIME.year if CURRENT_TIME.month == 12 else CURRENT_TIME.year - 1

for year in range(2015, MOST_RECENT_DECEMBER_YEAR+1):
    try:
        import_module(f'.year_{year}', package='advent_of_code_explainer.puzzles')
    except ModuleNotFoundError:
        pass
