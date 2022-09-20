'''
This is the mc module.

This is the docstring, you can write documentation in here.

>>> m = Markov('ab')
>>> m
'object string'
>>> m.predict('a')
'b'
'''

class Markov:
    def __init__(self, txt):
        self.table = None
        
    def predict(self, txt):
        return 'b'

# make a function that will create transition table
def get_table(txt):
    '''This is the get_table docstring
    >>> get_table('ab')
    {'a': {'b': 1}}
    '''
    results = {} # empty dictionary literal