'''
Siyi Ling
CS 5001, Fall 2022
Final Project

This is the testsuite for the School class.
'''

import unittest
from school import School

class SchoolTest(unittest.TestCase):
    '''Class SchoolTest
       A testsuite that tests the __init__, __str__,
       and __eq__ method of the School class.
    '''

    def test_init_basic(self):
        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        self.assertEqual(school1.name, "Alexander Academy")
        self.assertEqual(school1.coordinates, "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}")
        self.assertEqual(school1.area, "Downtown")
    
    def test_str_basic(self):
        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        self.assertEqual(school1.__str__(), "Alexander Academy")
    
    def test_eq_basic(self):
        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        school2 = School("Britannia Community Secondary", 
        "{""coordinates"": [-123.07192309841, 49.27523599085204], ""type"": ""Point""}", "Grandview-Woodland")
        school3 = School("Anchor Point Montessori", 
        "{""coordinates"": [-123.13091892226645, 49.277061847359775],  ""type"": ""Point""}", "Downtown")
        self.assertTrue(school1.__eq__(school3))
        self.assertFalse(school1.__eq__(school2))
        with self.assertRaises(ValueError):
            school1.__eq__(3)

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
