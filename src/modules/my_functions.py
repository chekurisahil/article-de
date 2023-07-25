import pandas as pd
import re
import article as a

def get_words_pos(file):
    '''
        Returns a list of every position a word count appears.

        Args:
            file: Path to the file to be read.
    '''
    word_lines = []
    f = open(file, 'r')
    doc = f.readlines()
    for index, line in enumerate(doc):
        if re.match(r'^[\d,]+ words$', line):
            word_lines.append(index)
    return word_lines

def get_article_list(file):
    '''
        Creates an Article object for every word count position and returns a list of the Article objects.

        Args:
            file: Path to the file to be read.
    '''
    word_lines = get_words_pos(file)
    article_list = []
    for id, word_line in enumerate(word_lines):
        article = a.Article(id, file, word_line)
        article_list.append(article)
    return article_list

def get_article_data(article):
    '''
        Gets values from an Article object, writes it to a Pandas DataFrame() and returns the DataFrame() object.


        Args:
            article: An Article object.
    '''
    df = pd.DataFrame({
        'Headline': [article.title],
        'Words': [article.words],
        'News Date': [article.date],
        'Source': [article.source]
    })
    
    df['News Date'] = pd.to_datetime(df['News Date'], format='%d %B %Y')
    df['News Date'] = df['News Date'].dt.strftime('%m/%d/%y')
    return df