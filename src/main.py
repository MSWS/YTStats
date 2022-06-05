import json

from evaulator import Evaluator
from entry import Entry


def init():
    evaluator = Evaluator()
    with open('debug-data.json', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            evaluator.addEntry(Entry(entry))
    evaluator.generate()


if __name__ == '__main__':
    init()
