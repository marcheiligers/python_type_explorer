import unittest
from type_explorer import *

class TestTypeExplorer(unittest.TestCase):

  def test_is_interesting(self):
    self.assertTrue(TypeExplorer([]).is_interesting())
    self.assertTrue(TypeExplorer({}).is_interesting())
    self.assertFalse(TypeExplorer("").is_interesting())
    self.assertFalse(TypeExplorer(1).is_interesting())

if __name__ == '__main__':
    unittest.main()