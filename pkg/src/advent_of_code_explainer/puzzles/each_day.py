from abc import ABC, abstractmethod


class EachDay(ABC):
    @staticmethod
    @abstractmethod
    def solve_one(number):
        pass

    @staticmethod
    @abstractmethod
    def solve_two(number):
        pass
