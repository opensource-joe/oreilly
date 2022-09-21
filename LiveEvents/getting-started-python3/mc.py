'''
This is the mc module.

This is the docstring, you can write documentation in here.

>>> m = Markov('ab')
>>> m
'object string'
>>> m.predict('a')
'b'
'''
import random

class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)
        
    def predict(self, txt):
        options = self.table.get(txt, {})
        if not options:
            raise KeyError(f'{txt} not found')
        letters = []
        for letter in options:
            count = options[letter]
            for i in range(count):
                letters.append(letter)
        return random.choice(letters)

# make a function that will create transition table
def get_table(txt):
    '''This is the get_table docstring
    >>> get_table('ab')
    {'a': {'b': 1}}  # nested dictionary where a is key for value of b:1
    '''
    results = {} # empty dictionary literal
    for i in range(len(txt)):
        char = txt[i]
        try:
            dst = txt[i+1]
        except IndexError:
            break
        if char in results:
            char_dict = results[char]
        else:
            char_dict = {}
        if dst not in char_dict:
            char_dict[dst] = 0
        char_dict[dst] += 1
        results[char] = char_dict
    return results