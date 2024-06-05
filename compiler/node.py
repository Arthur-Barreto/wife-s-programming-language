from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, value: any, children: list):
        self.value = value
        self.children = children

    @abstractmethod
    def evaluate(self, symble_table):
        pass
