# Marcel Champagne, 52532335, Lab Sect. 6 Assignment 3.

import urllib.request

def return_url_content(url: str) -> None:
    '''Returns a list of the contents of an url split, with the lines split into a list.'''
    
    with urllib.request.urlopen(url) as data:
        data_bytes = data.read()
        
    data_string = data_bytes.decode(encoding='utf-8')
    content = data_string.splitlines()

    return content
