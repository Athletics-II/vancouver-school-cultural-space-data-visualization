'''
Siyi Ling
CS 5001, Fall 2022
Final Project

This is the testsuite for the Area class.
'''

import unittest
from area import Area
from school import School
from culturalspace import CulturalSpace

class AreaTest(unittest.TestCase):
    '''Class AreaTest
       Tests the __init__, __str__, __eq__
       and additional methods of the Area class.
    '''

    def test_init_basic(self):
        area1 = Area("Downtown")
        self.assertEqual(area1.name, "Downtown")
    
    def test_str_basic(self):
        area1 = Area("Downtown")
        self.assertEqual(area1.__str__(), "Downtown")
    
    def test_eq_basic(self):
        area1 = Area("Downtown")
        area2 = Area("Downtown")
        area3 = Area("Kitsilano")
        self.assertTrue(area1.__eq__(area2))
        self.assertFalse(area1.__eq__(area3))
        with self.assertRaises(ValueError):
            area1.__eq__(3)
    
    def test_update_school_list(self):
        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        school2 = School("Britannia Community Secondary", 
        "{""coordinates"": [-123.07192309841, 49.27523599085204], ""type"": ""Point""}", "Grandview-Woodland")
        school3 = School("Anchor Point Montessori", 
        "{""coordinates"": [-123.13091892226645, 49.277061847359775],  ""type"": ""Point""}", "Downtown")

        schools = [school1, school2, school3]
        area1 = Area("Downtown")
        area1.update_school_list(schools)
        self.assertEqual(area1.school_list, [school1, school3])
    
    def test_update_cultural_space_list(self):
        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        culturalspace2 = CulturalSpace("222 E Georgia Studios", "Studio/Rehearsal", "Strathcona", 
        "{""coordinates"": [-123.098829,  49.278453],  ""type"": ""Point""}")
        culturalspace3 = CulturalSpace("Alliance for Arts and Culture", "Museum/Gallery", "Downtown", 
        "{""coordinates"": [-123.1228359,  49.2803099],  ""type"": ""Point""}")

        cultural_spaces = [culturalspace1, culturalspace2, culturalspace3]
        area1 = Area("Strathcona")
        area1.update_cultural_space_list(cultural_spaces)
        self.assertEqual(area1.cultural_space_list, [culturalspace1, culturalspace2])
    
    def test_count_cultural_space_per_school(self):
        area1 = Area("Downtown")

        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        school2 = School("Britannia Community Secondary", 
        "{""coordinates"": [-123.07192309841, 49.27523599085204], ""type"": ""Point""}", "Grandview-Woodland")
        school3 = School("Anchor Point Montessori", 
        "{""coordinates"": [-123.13091892226645, 49.277061847359775],  ""type"": ""Point""}", "Downtown")
        schools = [school1, school2, school3]
    
        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        culturalspace2 = CulturalSpace("222 E Georgia Studios", "Studio/Rehearsal", "Strathcona", 
        "{""coordinates"": [-123.098829,  49.278453],  ""type"": ""Point""}")
        culturalspace3 = CulturalSpace("Alliance for Arts and Culture", "Museum/Gallery", "Downtown", 
        "{""coordinates"": [-123.1228359,  49.2803099],  ""type"": ""Point""}")
        cultural_spaces = [culturalspace1, culturalspace2, culturalspace3]

        area1.update_school_list(schools)
        area1.update_cultural_space_list(cultural_spaces)
        area1.count_cultural_space_per_school()
        self.assertEqual(area1.cultural_space_per_school, 0.5)
    
    def test_update_cultural_space_type_dict(self):
        area1 = Area("Downtown")

        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        culturalspace2 = CulturalSpace("222 E Georgia Studios", "Studio/Rehearsal", "Strathcona", 
        "{""coordinates"": [-123.098829,  49.278453],  ""type"": ""Point""}")
        culturalspace3 = CulturalSpace("Alliance for Arts and Culture", "Museum/Gallery", "Downtown", 
        "{""coordinates"": [-123.1228359,  49.2803099],  ""type"": ""Point""}")
        cultural_spaces = [culturalspace1, culturalspace2, culturalspace3]

        area1.update_cultural_space_list(cultural_spaces)
        area1.update_cultural_space_type_dict()
        self.assertEqual(area1.cultural_space_type_dict, {"Museum/Gallery": 1.0})
    
    def test_count_cultural_space_type_per_school(self):
        area1 = Area("Downtown")

        school1 = School("Alexander Academy", 
        "{""coordinates"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}", "Downtown")
        school2 = School("Britannia Community Secondary", 
        "{""coordinates"": [-123.07192309841, 49.27523599085204], ""type"": ""Point""}", "Grandview-Woodland")
        school3 = School("Anchor Point Montessori", 
        "{""coordinates"": [-123.13091892226645, 49.277061847359775],  ""type"": ""Point""}", "Downtown")
        schools = [school1, school2, school3]

        culturalspace1 = CulturalSpace("221A Artist Run Centre", "Museum/Gallery", "Strathcona", 
        "{""coordinates"": [-123.098796,  49.278786],  ""type"": ""Point""}")
        culturalspace2 = CulturalSpace("222 E Georgia Studios", "Studio/Rehearsal", "Strathcona", 
        "{""coordinates"": [-123.098829,  49.278453],  ""type"": ""Point""}")
        culturalspace3 = CulturalSpace("Alliance for Arts and Culture", "Museum/Gallery", "Downtown", 
        "{""coordinates"": [-123.1228359,  49.2803099],  ""type"": ""Point""}")
        cultural_spaces = [culturalspace1, culturalspace2, culturalspace3]

        area1.update_school_list(schools)
        area1.update_cultural_space_list(cultural_spaces)
        area1.update_cultural_space_type_dict()
        area1.count_cultural_space_type_per_school()
        self.assertEqual(area1.cultural_space_type_per_school, {"Museum/Gallery": 0.5})
    
def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()


