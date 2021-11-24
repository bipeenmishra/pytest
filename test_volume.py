import unittest
from statistics import mean
import numpy
import pandas as pd
df2 = pd.read_csv('C:\\Users\\mishr\\Downloads\\demo_data_churn.csv', engine='python')
sum_val = 256677722.91003045
mean_val = 788.2278317708805
max_val = 439245.0136
min_val = -1220509.226
median_val = 40.35166904
std_val = 6755.173313682895
var_val = 45632366.49789355

# Testing for volume data


class TestingSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(df2['volume_in_kg']), sum_val, )

    def test_mean(self):
        self.assertEqual(numpy.mean(df2['volume_in_kg']),mean_val, )

    def test_max(self):
        self.assertEqual(numpy.max(df2['volume_in_kg']), max_val, )

    def test_min(self):
        self.assertEqual(numpy.min(df2['volume_in_kg']), min_val,)

    def test_median(self):
        self.assertEqual(numpy.median(df2['volume_in_kg']), median_val,)

    def test_std(self):
        self.assertEqual(numpy.std(df2['volume_in_kg']), std_val,)

    def test_var(self):
        self.assertEqual(numpy.var(df2['volume_in_kg']), var_val,)


if __name__ == '__main__':
    unittest.main()


