import unittest
from statistics import mean
import numpy
import pandas as pd

df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
sum_val = 2719153786.144917
mean_val = 8350.209238282016
max_val = 3077822.953
min_val = -3221995.235
median_val = 1810.978448
std_val = 29363.13365365425
var_val = 862193617.9623628


# Testing for sales data


class TestingSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(numpy.sum(df2['gross_sales']), sum_val, )

    def test_mean(self):
        self.assertEqual(numpy.mean(df2['gross_sales']), mean_val, )

    def test_min(self):
        self.assertEqual(numpy.min(df2['gross_sales']), min_val, )

    def test_max(self):
        self.assertEqual(numpy.max(df2['gross_sales']), max_val, )

    def test_median(self):
        self.assertEqual(numpy.median(df2['gross_sales']), median_val, )

    def test_std(self):
        self.assertEqual(numpy.std(df2['gross_sales']), std_val, )

    def test_var(self):
        self.assertEqual(numpy.var(df2['gross_sales']), var_val, )


if __name__ == '__main__':
    unittest.main()
