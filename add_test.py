import unittest
from add import add
import random

class FreeTest(unittest.TestCase):
    def runTest(self):
        pass

class BasciTest(unittest.TestCase):
    def runTest(self):
        a, b = 2, 2
        assert add(a, b) == 4, '2 + 2 doesn\'t equal 4, uh oh'

class ComplexTest(unittest.TestCase):
    def runTest(self):
        n = random.randint(1, 50)
        l = [random.randint(-100, 100) for _ in range(n)]
        assert add(*l) == sum(l)

if __name__ == "__main__":
    unittest.main()
