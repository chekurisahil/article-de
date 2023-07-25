# Article Data Extraction

This tool goes through a .txt file of articles and outputs identifying information about each article into an Excel file. Each row in the outputted Excel file represents one article and contains information such as headline, word count, news date, and source. A new Excel file is created for every file read.


## Table of Contents

- Usage
- Documentation
- Installation
- Configuration

## Usage 

1. Install this program.
2. Convert all .rtf files to .txt files and put



This module requires the following modules:
- [Bad judgement](https://www.drupal.org/project/bad_judgement)

OR

This module requires no modules outside of Drupal core.

## Documentation
// main function in 2-3 sentences. my_functions() 

// functions are in my_functions().py. 

// Article class has all the logic to extract data from an article.

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

- `__init__()`
	- Creates the Article object and sets `id`, `file`, and `words_pos`
- `set_values()`
	- Searches through lines near the word count to identify and set  `words`, `date`, `source`, and `title`
- `similarity()`
	- Compares 2 strings and returns a similarity score between 0 and 1
- `get_article_titles()`
	- Returns a list of article titles  `id`, `file`, and `words_pos`


### MODULE: my_functions.py

This module contains functions that are used to get information about the Article objects:

- `get_words_pos()`
	- Returns a list of every position a word count appears
- `get_article_list()`
	- Creates an Article object for every word count position and returns a list of the Article objects
- `get_article_data()`
	- Gets values from Article object, writes it to a Pandas DataFrame() and returns the DataFrame() object




## Installation (required, unless a separate INSTALL.md is provided)

- Need python installed on your laptop
- give instructions
- directory structure
- 


Install as you would normally install a contributed Drupal module. For further information, see [Installing Drupal Modules](https://www.drupal.org/docs/extending-drupal/installing-drupal-modules).


## Configuration (required)

1. Enable the module at Administration > Extend.
1. Profit.