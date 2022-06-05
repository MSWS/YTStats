import datetime
import re

class Entry:
    def __init__(self, data):
        self.data = data
        self.header = data['header']
        self.title: str = data['title']
        if self.title.startswith("Watched "):
            self.title = self.title[8:]
        self.plainTitle = re.sub(self.title.lower(), "[^a-z\s]", "")
        self.url = data['titleUrl']
        self.date = datetime.datetime.strptime(
            data['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
        self.channel = data['subtitles'][0]['name']
        self.channelUrl = data['subtitles'][0]['url']

    def __str__(self):
        return self.data['title']
