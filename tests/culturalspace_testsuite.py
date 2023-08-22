'''
Siyi Ling
CS 5001, Fall 2022
Final Project

This is the testsuite for the CulturalSpace class.
'''

import unittest
from culturalspace import CulturalSpace

class CulturalSpaceTest(unittest.TestCase):
    '''Class CulturalSpaceTest
       A testsuite that tests the __init__, __str__,
       and __eq__ method of the CulturalSpace class.
    '''
    def test_init_basic(self):
        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        self.assertEqual(culturalspace1.name, "221A Artist Run Centre")
        self.assertEqual(culturalspace1.type, "Museum/Gallery")
        self.assertEqual(culturalspace1.area, "Strathcona")
        self.assertEqual(culturalspace1.coordinates, "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")

    def test_str_basic(self):
        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        self.assertEqual(culturalspace1.__str__(), "221A Artist Run Centre")
    
    def test_eq_basic(self):
        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        culturalspace2 = CulturalSpace("222 E Georgia Studios", "Studio/Rehearsal", "Strathcona", 
        "{""coordinates"": [-123.098829,  49.278453],  ""type"": ""Point""}")
        culturalspace3 = CulturalSpace("Alliance for Arts and Culture", "Museum/Gallery", "Downtown", 
        "{""coordinates"": [-123.1228359,  49.2803099],  ""type"": ""Point""}")
        self.assertTrue(culturalspace1.__eq__(culturalspace2))
        self.assertFalse(culturalspace1.__eq__(culturalspace3))
        with self.assertRaises(ValueError):
            culturalspace1.__eq__(3)

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()