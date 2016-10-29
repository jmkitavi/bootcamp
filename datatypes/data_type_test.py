import unittest
import datatype

class DataTypeTestCase(unittest.TestCase):

  def test_none_type(self):
    self.assertEqual('no value', datatype.data_type(None))

  def test_array_type(self):
    self.assertEqual(3, datatype.data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, datatype.data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, datatype.data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', datatype.data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', datatype.data_type(200))

  def test_str_type(self):
    self.assertEqual(6, datatype.data_type('andela'))