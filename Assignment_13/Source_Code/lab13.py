import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEuqla(result, 0, 'The total function should return 0')

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, 12, 4, 'The average function should return 12')

    def test_average_returns_nan(self):
        result = Grades.average([])
