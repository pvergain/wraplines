"""Format and sanitize a text.


"""

import textwrap

# https://github.com/google/python-fire/blob/master/docs/guide.md
# pipenv install fire
import fire

# https://ftfy.readthedocs.io/en/latest/
# pipenv install ftfy
from ftfy import fix_text

def wrap(input_file, max_length=80):
    """Format a text to max_length characters.

    - the first step is to remove the line feeds.
    - the second step is to format line to 80 characters.
    - the third step is to remove extra spaces
    
	Args:
		input_file (str) : the filename. 
		max_length (int) : the max length of the line   

    Calling example::
    
        pipenv run python wrap.py wrap input.txt

    or::

        pipenv run python wrap.py wrap input.txt 70
            
    """
    with open(input_file, 'r') as f:
        text = f.read()


    # remove the moji-bakes
    # https://ftfy.readthedocs.io/en/latest/#using-ftfy
    text = fix_text(text)

    # remove the line feeds
    long_text = text.rstrip()
    
    # format line to length characters
    long_text_string = textwrap.fill(long_text, max_length)
    for espaces in [
        '     ',
        '    ',
        '   ',
        '  ',
    ]:
        # remove extra spaces
        long_text_string = long_text_string.replace(espaces, ' ')
        
    print(long_text_string)


if __name__ == '__main__':
    fire.Fire()
