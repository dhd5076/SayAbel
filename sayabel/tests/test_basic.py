import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sayabel import *

class MarkovTests(unittest.TestCase):

    def testMarv(self):
        chain = Markov()
        self.assertEqual()

