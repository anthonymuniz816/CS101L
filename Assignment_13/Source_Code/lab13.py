#Anthony Muniz
#Program 13
#CS 101 Lab

#ALGORITHM:
#START
#Import math, unittest and the Grades file
#Create a class
#Within class create function that will test the total function
#Create another function that will test the total function if it is empty
#Create another function that will test the average function
#create another function that will test the average function if it returns 0
#Create another fucntion that will test the average function again
#Create another function that will test the average function if it returns nan
#Create another function that will test the median function if it is even
#Create another function that will test the median function if it is odd
#Create another function that will test the median function if it is empty
#Call unittest in the main
#END
import math
import unittest
import Grades

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result, 33)

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0)

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, 5.3333, 4)

    def test_average_two(self):
        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12, 4)

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(result,math.nan,)

    def test_median_even(self):
        result = Grades.median([3,5,2,1])
        self.assertAlmostEqual(result,2.5)

    def test_median_odd(self):
        result = Grades.median([3,7,2])
        self.assertIs(result,3)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
        

unittest.main()
