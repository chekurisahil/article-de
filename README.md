# Article Data Extraction
<img src='https://img.shields.io/badge/Python-3776AB?style=plastic&logo=python&logoColor=white'> <img src='https://img.shields.io/badge/Excel-217346?style=plastic&logo=microsoft-excel&logoColor=white'> 

This program saves time for researchers looking for information about articles. It reads through all the articles in a TXT file and outputs the headline, word count, news date, and source into an Excel file with the same name.

This program can be enhanced to extract other information.

## How It Works

This program is written in Python. It starts by finding the positions of the word counts of the articles in the TXT file and generates a list of all the articles. The list is iterated over and individual pieces of information for each article are gathered into a list. Once the list is complete, it is written into an Excel file.

## Technical Details

This program uses the **os**, **pandas**, **re**, **datetime**, and **difflib** packages. If you don't have these packages, use the pip install command to install them.

To use this program, clone the GitHub repository and once you have all the TXT files in the data/txt directory, execute the command:
```
python3 main.py
```
Once the command finishes, go to the output directory, and all the Excel files should be there.

## Reference

### MODULE: article.py

This module defines a class that contains attributes for an Article object. This object contains defining information such as:

- `file_name` - file in which Article is found
- `id` - order of the article in the file
- `words_pos` - position of the word count
- `words` - word count
- `date` - date of publishing
- `source` - publishing source
- `title` - headline of the article

This module also has primary functions that either set the above attributes or help to set the attributes.

| Function  | Description | 
| --------- | ----------- | 
| `__init__()`   | Creates the Article object and sets `id`, `file`, and `words_pos` |
| `set_values()` | Searches through lines near the word count to identify and set  `words`, `date`, `source`, and `title` |
| `similarity()` | Compares 2 strings and returns a similarity score between 0 and 1 | 
| `get_article_titles()` | Returns a list of article titles  `id`, `file`, and `words_pos` |

### MODULE: my_functions.py

This module contains functions that are used to get information about the Article objects:

| Function  | Description | 
| --------- | ----------- | 
| `get_words_pos()` | Returns a list of every position a word count appears |
| `get_article_list()` | Creates an Article object for every word count position and returns a list of the Article objects |
| `get_article_data()` | Gets values from the Article object, writes it to a Pandas DataFrame() and returns the DataFrame() object |

## Support

In case you have questions, please reach out to Sahil Chekuri at schekur1@uci.edu.
