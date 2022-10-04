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
def get_table(txt, size=1): # change in code = !!!
    '''This is the get_table docstring
    >>> get_table('ab')
    {'a': {'b': 1}}  # nested dictionary where a is key for value of b:1
    '''
    results = {} # empty dictionary literal
    for i in range(len(txt)):
        chars = txt[i:i+size] # !!!
        try:
            dst = txt[i+size] # !!!
        except IndexError:
            break
        char_dict = results.get(chars, {}) # !!!
        char_dict.setdefault(dst, 0)
        char_dict[dst] += 1
        results[chars] = char_dict # !!!
    return results