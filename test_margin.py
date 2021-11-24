import unittest
from statistics import mean
import numpy
import pandas as pd
df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
sum_val = 1457317609.7210157
mean_val = 4475.255143643776
max_val = 3073251.674
min_val = -4069043.765
median_val = 760.69374
std_val = 24221.48897785519
var_val = 586680528.3043605

# Testing for margin data


class TestingSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(numpy.sum(df2['gm']), sum_val, )

    def test_mean(self):
        self.assertEqual(numpy.mean(df2['gm']), mean_val, )

    def test_min(self):
        self.assertEqual(numpy.min(df2['gm']), min_val, )

    def test_max(self):
        self.assertEqual(numpy.max(df2['gm']), max_val, )

    def test_median(self):
        self.assertEqual(numpy.median(df2['gm']), median_val, )

    def test_var(self):
        self.assertEqual(numpy.var(df2['gm']), var_val, )

    def test_std(self):
        self.assertEqual(numpy.std(df2['gm']), std_val, )


if __name__ == '__main__':
    unittest.main()
