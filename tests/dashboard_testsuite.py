'''
Siyi Ling
CS 5001, Fall 2022
Final Project

This is the testsuite for the dashboard driver file.
'''
import unittest
from data_dashboard import *
from school import School
from culturalspace import CulturalSpace
from area import Area

class DashboardTest(unittest.TestCase):
    '''Class DashboardTest
       Tests the functions in the data_dashboard driver file.
    '''

    def test_open_csv_basic(self):
        test_data = open_csv("https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        self.assertEqual(test_data[:8], "ADDRESS;")

    def test_clean_school_data_basic(self):
        school_data = '998 W 26th Av;Independent School;Vancouver Talmud Torah Elementary;"{""coordinates"": [-123.12682202118758, 49.2475796718668], ""type"": ""Point""}";South Cambie\n15 N Renfrew St;Independent School;West Coast Christian School;"{""coordinates"": [-123.04453612333309, 49.284984466234356], ""type"": ""Point""}";Hastings-Sunrise\n4125 W 8th Av;Independent School;West Point Grey Academy;"{""coordinates"": [-123.20150739365414, 49.26706634514379], ""type"": ""Point""}";West Point Grey'

        school_name, school_coord, school_area = clean_school_data(school_data)
        self.assertEqual(school_name, ['West Coast Christian School'])
        self.assertEqual(school_coord, ['"{""coordinates"": [-123.04453612333309, 49.284984466234356], ""type"": ""Point""}"'])
        self.assertEqual(school_area, ['Hastings-Sunris'])

    def test_clean_school_data_bad(self):
        with self.assertRaises(TypeError):
            clean_school_data([1, 2, 3])
    
    def test_create_school_obj(self):
        school_name = ['West Coast Christian School']
        school_coord = ['{""coordinates"": [-123.04453612333309, 49.284984466234356], ""type"": ""Point""}']
        school_area = ['Hastings-Sunrise']
        schools = create_school_obj(school_name, school_coord, school_area)
        self.assertEqual(schools[0].__str__(), "West Coast Christian School")

    def test_clean_cultural_space_data(self):
        cultural_space_data = '2017;222 E Georgia Studios;http://projectspace.ca/blog/;Studio/Rehearsal;Artist Studio;222 E Georgia St, Vancouver, BC, V6A 1Z7;Strathcona;Privately Owned;7800;;Yes;"{""coordinates"": [-123.098829, 49.278453], ""type"": ""Point""}"\n2017;221A Artist Run Centre;www.221a.ca/?;Museum/Gallery;Museum/Gallery;221 E Georgia St, Vancouver, BC, V6A 1Z6;Strathcona;Privately Owned;9000;;Yes;"{""coordinates"": [-123.098796, 49.278786], ""type"": ""Point""}"\n2017;Aberthau Mansion/West Point Grey Community Centre;;Community Space;Community Centre/Hall;4397 W 2nd Av, Vancouver, BC, V6R 1K4;West Point Grey;City of Vancouver;2930;;Yes;"{""coordinates"": [-123.205213, 49.271511], ""type"": ""Point""}"'

        cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord = clean_cultural_space_data(cultural_space_data)
        self.assertEqual(cultural_space_name, ['221A Artist Run Centre'])
        self.assertEqual(cultural_space_type, ['Museum/Gallery'])
        self.assertEqual(cultural_space_area, ['Strathcona'])
    
    def test_clean_cultural_space_data_bad(self):
        with self.assertRaises(TypeError):
            clean_cultural_space_data([1, 2, 3])
    
    def test_create_cultural_space_obj(self):
        cultural_space_name = ['221A Artist Run Centre']
        cultural_space_type = ['Museum/Gallery']
        cultural_space_area = ['Strathcona']
        cultural_space_coord = ['"{""coordinates"": [-123.098796, 49.278786], ""type"": ""Point""}"']
        cultural_spaces = create_cultural_space_obj(cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord)
        self.assertEqual(cultural_spaces[0].__str__(), '221A Artist Run Centre')

    def test_create_unique_area_list(self):
        unique_area = create_unique_area_list(['Downtown', 'Kitsilano', 'Downtown'])
        self.assertEqual(unique_area, ['Downtown', 'Kitsilano'])
    
    def test_create_area_obj(self):
        unique_areas = ['Downtown']
        areas = create_area_obj(unique_areas)
        self.assertEqual(areas[0].__str__(), "Downtown")
    
    def test_build_school_cs_dict_sort_by_area(self):
        area1 = Area('Mount-Pleasant')
        area2 = Area('Downtown')
        areas = [area1, area2]
        sorted_by_area = build_school_cs_dict_sort_by_area(areas)
        self.assertEqual(sorted_by_area, {'Downtown': 0.0, 'Mount-Pleasant': 0.0})

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
