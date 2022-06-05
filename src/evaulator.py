from typing import Any, OrderedDict
from entry import Entry


class Evaluator:
    def __init__(self):
        self.entries = {}
        self.authors = {}
        self.aliases = {}
        self.titles = []
        self.words = {}

    def addEntry(self, entry: Entry):
        self.entries[entry.date] = entry
        print(entry, type(entry))
        self.authors.setdefault(entry.channelUrl, [])
        self.authors[entry.channelUrl].append(entry)
        self.aliases.setdefault(entry.channelUrl, [])
        self.aliases[entry.channelUrl].append(entry.channel)
        self.titles.append(entry.title)
        for word in entry.plainTitle.split():
            if word not in self.words:
                self.words[word] = 0
            self.words[word] += 1

    def generate(self):

        print(self.authors, self.aliases, self.titles, self.words, sep='\n')
