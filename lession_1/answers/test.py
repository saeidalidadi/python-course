import sys
from os import listdir, path
from os.path import isfile, join
import unittest

sys.dont_write_bytecode = True

class TestNameAge(unittest.TestCase):
  def test_template(self):
    dirname = path.dirname(path.realpath(__file__))
    answers_by_name = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    for answer in answers_by_name:
      if answer == 'test.py':
        continue
      moded = __import__(answer.rsplit('.')[0])
      first_name = "Saeid"
      age = 31
      self.assertEqual(
        moded.my_function(first_name, age),
        "My name is " + first_name + " and I am " + str(age) +" years old."
      )

if __name__ == "__main__":
  unittest.main()