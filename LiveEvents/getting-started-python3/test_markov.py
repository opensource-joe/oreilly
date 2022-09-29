import unittest
from unittest import result
import mc

class TestMarkov(unittest.TestCase):
    def test_get_table(self):
        # 1 - setup
        result = mc.get_table('ab') # 2 - call unit
        # 3 - make assertion
        self.assertEqual(result, {'a': {'b': 1}})
        # 4 - teardown

    def test_get_table2(self):
        result = mc.get_table('abacab')
        self.assertEqual(result, {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}})
    
    def test_predict(self):
        m = mc.Markov('xyz') # 1 - setup
        result = m.predict('x') # 2 - call unit
        self.assertEqual(result, 'y') # 3 - make assertion
        # 4 - cleanup

if __name__ == '__main__':
    unittest.main()
else:
    print('importing as library')