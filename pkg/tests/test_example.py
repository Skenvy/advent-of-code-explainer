# import pytest
from src import advent_of_code_explainer as aoce


def test_function():
    assert aoce.__version__ == "0.0.1"
    assert aoce.puzzles.year_2024.day_1.add_one(0) == 1
