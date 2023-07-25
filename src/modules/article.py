import re
from datetime import datetime as dt
import difflib

class Article:
    file_name = None
    id = None
    
    words_pos = None
    words = None
    date = None
    source = None
    title = None

    def __init__(self, id, file, words_pos):
        self.id = id
        self.file = file
        self.words_pos = words_pos
        self.set_values()


    def set_values(self):
        f = open(self.file, 'r')
        doc = f.readlines()
        article_titles = self.get_article_titles(doc)

        for i in range(self.words_pos-4, self.words_pos+6):
            line = doc[i].strip()
            if re.match(r'^[\d,]+ words$', line): 
                self.words = line.split()[0].replace(',', '')
            if re.match(r'\d{1,2} [A-Z]\w{1,} \d{4}', line): 
                self.date = line.strip()
                if re.match(r'\d{1,2}:\d{1,2} [AP]M', doc[i+1]):
                    self.source = doc[i+2]
                else:
                    self.source = doc[i+1]
            if line in article_titles:
                self.title = line
            else:
                for title in article_titles:
                    if self.similarity(line, title) > 0.5:
                        self.title = line
        

    def similarity(self, str1, str2):
        return difflib.SequenceMatcher(None, str1, str2).ratio()


    def get_article_titles(self, document):
        article_titles = []
        for line in document:
            if ord(line[0]) == 8226:
                article_titles.append(line[1:].strip())
        return article_titles

def test():
        a = Article(1, './data/txt/Walmart - 1-27-2014.txt', 30)
        f = open(a.file, 'r')
        doc = f.readlines()
        print(a.words_pos)