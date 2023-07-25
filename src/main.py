import sys
sys.path.append('./src/modules')

import os
import pandas as pd
from my_functions import *

data_dir = './data/txt'
output_dir = './output'

for file in os.listdir(data_dir):
    file_path = data_dir + '/' + file
    file_xl = file.replace('.txt', '.xlsx')
    article_list = get_article_list(file_path)
    df = None
    for article in article_list:
        article_df = get_article_data(article)
        if not isinstance(df, pd.DataFrame):
            df = article_df
        else:
            df = df._append(article_df, ignore_index=True)
    df.to_excel(output_dir + '/' + file_xl)
