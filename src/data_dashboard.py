'''
Siyi Ling
CS 5001, Fall 2022
Final Project

This is the dashboard driver file for school-cultural space analysis program.
'''

import requests
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from school import School
from culturalspace import CulturalSpace
from area import Area

ROOT_TITLE = "Cultural Space and School Analysis Visuals"
ROOT_SIZE = "450x300"

SCHOOL_NAME_IND = 2
SCHOOL_COORD_IND = 3
SCHOOL_AREA_IND = 4

CULTURAL_SPACE_NAME_IND = 1
CULTURAL_SPACE_TYPE_IND = 3
CULTURAL_SPACE_AREA_IND = 6
CULTURAL_SPACE_COORD_IND = 9

BAR_HEIGHT = 0.7
BAR_COLOR = "#678983"
TEXT_COLOR = "#181D31"
TEXT_SIZE = "medium"
PLOT_TITLE = "Unit of Cultural Space per School on Average"
PLOT_STYLE = "Solarize_Light2"
BAR_PADDING = 1.08

def open_csv(file_url):
    '''Function open_csv
       Input: file
       Returns: str

       Does: opens and reads the designated file, handles Connection and HTTP errors as appropriate
    '''
    try:
        file = requests.get(file_url)
        file.raise_for_status()
        file_data = file.text
    except ConnectionError as ex:
        print("Invalid type:", ex)
    except requests.exceptions.HTTPError as ex:
        print("Invalid type:", ex)

    return file_data

def clean_school_data(school_data):
    '''Function clean_school_data
       Input: str
       Returns: tuple of lists

       Does: sorts information in file into separate lists, handles TypeError as appropriate
    '''
    if not isinstance(school_data, str):
        raise TypeError("Original data on schools must be a string.")

    school_data_split = school_data.split("\n")

    school_name = []
    school_coord = []
    school_area = []

    #slice the list to exclude header and the empty last line
    for item in school_data_split[1: -1]:
        school_name.append(item.split(";")[SCHOOL_NAME_IND])
        school_coord.append(item.split(";")[SCHOOL_COORD_IND])
        school_area.append(item.split(";")[SCHOOL_AREA_IND][: -1])

    return school_name, school_coord, school_area

def create_school_obj(school_name, school_coord, school_area):
    '''Function create_school_obj
       Input: lists (of str, )
       Returns: list of objs

       Does: creates a list of School objs
    '''
    schools = []

    for i in range(len(school_name)):
        schools.append(School(school_name[i], school_coord[i], school_area[i]))

    return schools
    
def clean_cultural_space_data(cultural_space_data):
    '''Function clean_cultural_space_data
       Input: str
       Returns: tuple of lists

       Does: sorts information in file into separate lists, handles TypeError as appropriate
    '''
    if not isinstance(cultural_space_data, str):
        raise TypeError("Original data on cultural spaces must be a string.")

    cultural_space_data_split = cultural_space_data.split("\n")

    cultural_space_name = []
    cultural_space_type = []
    cultural_space_area = []
    cultural_space_coord = []

    for item in cultural_space_data_split[1: -1]:
        cultural_space_name.append(item.split(";")[CULTURAL_SPACE_NAME_IND])
        cultural_space_type.append(item.split(";")[CULTURAL_SPACE_TYPE_IND])
        cultural_space_area.append(item.split(";")[CULTURAL_SPACE_AREA_IND])
        cultural_space_coord.append(item.split(";")[CULTURAL_SPACE_COORD_IND])

    return cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord

def create_cultural_space_obj(cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord):
    '''Function create_cultural_space_obj
       Input: tuple of lists
       Returns: list of objs

       Does: creates a list of CulturalSpace objs
    '''
    cultural_spaces = []

    for i in range(len(cultural_space_name)):
        cultural_spaces.append(CulturalSpace(cultural_space_name[i], cultural_space_type[i], 
        cultural_space_area[i], cultural_space_coord[i]))

    return cultural_spaces

def create_unique_area_list(school_area):
    '''Function create_unique_area_obj
       Input: lst
       Returns: lst

       Does: drops iterations of areas, creates a list of unique areas
    '''
    unique_areas = []

    for area in school_area:
        if area not in unique_areas:
            unique_areas.append(area)

    return unique_areas
    
def create_area_obj(unique_areas):
    '''Function create_area_obj
       Input: lst
       Returns: list of objs

       Does: creates a list of Area objs, handles TypeError as appropriate
    '''
    areas = []

    for i in range(len(unique_areas)):
        areas.append(Area(unique_areas[i]))

    return areas

def analyze_school_cultural_space(areas, schools, cultural_spaces):
    '''Function analyze_school_cultural_space
       Input: lst
       Returns: none
    
       Does: produces the calculated units of cultural space
       in different areas and units of cultural space types
    '''
    for area in areas:
        area.update_school_list(schools)
        area.update_cultural_space_list(cultural_spaces)
        area.count_cultural_space_per_school()
        area.update_cultural_space_type_dict()
        area.count_cultural_space_type_per_school()

def build_school_cs_dict_sort_by_area(areas):
    '''Function build_school_cs_dict_sort_by_area
       Input: list of objs
       Returns: dict

       Does: builds a dict to store areas and units of
       cultural space as key-value pairs, is sorted by area
       names in descending order; change reverse to True to
       sort in ascending order
    '''
    temp_dict = {}

    for area in areas:
        temp_dict[area.name] = area.cultural_space_per_school

    temp_list = sorted(((k, v) for (k, v) in temp_dict.items()), reverse = True)
    school_cs_dict_sort_by_area = dict([(k, v) for k, v in temp_list])

    return school_cs_dict_sort_by_area

def build_school_cs_dict_sort_by_units(areas):
    '''Function build_school_cs_dict_sort_by_units
       Input: list of objs
       Returns: dict

       Does: builds a dict to store areas and units of
       cultural space as key-value pairs, is sorted by units
       of cultural spaces in ascending order
    '''
    temp_dict = {}

    for area in areas:
        temp_dict[area.name] = area.cultural_space_per_school

    temp_list = sorted((v, k) for (k, v) in temp_dict.items())
    school_cs_dict_sort_by_units = dict([(k, v) for v, k in temp_list])

    return school_cs_dict_sort_by_units

def make_school_cs_bar_chart_sort_by_area(dict_by_area):
    '''Function make_school_cs_bar_chart_sort_by_area
       Input: dict
       Returns: none

       Does: visualizes the dict sorted by area name in
       a bar chart
    '''
    plt.style.use(PLOT_STYLE)

    x_axis_unit = list(dict_by_area.keys())
    y_axis_area = list(dict_by_area.values())
    plt.barh(x_axis_unit, y_axis_area, height = BAR_HEIGHT, color = BAR_COLOR)
    plt.title(PLOT_TITLE, fontdict = {"color": TEXT_COLOR, "fontsize": TEXT_SIZE})
    plt.xlabel("Unit of Cultural Space per School", fontdict = {"color": TEXT_COLOR, "fontsize": TEXT_SIZE})
    plt.tight_layout(pad = BAR_PADDING)

    plt.show()

def make_school_cs_bar_chart_sort_by_unit(dict_by_unit):
    '''Function make_school_cs_bar_chart_sort_by_unit
       Input: dict
       Returns: none

       Does: visualizes the dict sorted by unit of 
       cultural space in a bar chart
    '''
    plt.style.use(PLOT_STYLE)

    x_axis_unit = list(dict_by_unit.keys())
    y_axis_area = list(dict_by_unit.values())
    plt.barh(x_axis_unit, y_axis_area, height = BAR_HEIGHT, color = BAR_COLOR)

    plt.title(PLOT_TITLE, fontdict = {"color": TEXT_COLOR, "fontsize": TEXT_SIZE})
    plt.xlabel("Unit of Cultural Space per School", fontdict = {"color": TEXT_COLOR, "fontsize": TEXT_SIZE})
    plt.tight_layout(pad = BAR_PADDING)

    plt.show()

def make_downtown_pie_chart(areas):
    '''Function make_downtown_pie_chart
       Input: list of objs
       Returns: none

       Does: visualizes the cultural space type
       dict of downtown in a pie chart
    '''
    for area in areas:
        if area.name == "Downtown":
            pie_labels = list(area.cultural_space_type_per_school.keys())
            pie_slices = list(area.cultural_space_type_per_school.values())
            plt.pie(pie_slices, labels = pie_labels)
            plt.title("Cultural Space Types per School in Downtown")
            plt.tight_layout()
            plt.show()

def make_strathcona_pie_chart(areas):
    '''Function make_strathcona_pie_chart
       Input: list of objs
       Returns: none

       Does: visualizes the cultural space type
       dict of strathcona in a pie chart
    '''
    for area in areas:
        if area.name == "Strathcona":
            pie_labels = list(area.cultural_space_type_per_school.keys())
            pie_slices = list(area.cultural_space_type_per_school.values())
            plt.pie(pie_slices, labels = pie_labels)
            plt.title("Cultural Space Types per School in Strathcona")
            plt.tight_layout()
            plt.show()

def make_fairview_pie_chart(areas):
    '''Function make_fairview_pie_chart
       Input: list of objs
       Returns: none

       Does: visualizes the cultural space type
       dict of fairview in a pie chart
    '''
    for area in areas:
        if area.name == "Fairview":
            pie_labels = list(area.cultural_space_type_per_school.keys())
            pie_slices = list(area.cultural_space_type_per_school.values())
            plt.pie(pie_slices, labels = pie_labels)
            plt.title("Cultural Space Types per School in Fairview")
            plt.tight_layout()
            plt.show()

def sub_charts_callback(make_bar_chart_by_area, make_bar_chart_by_unit, 
dict_sort_by_area, dict_sort_by_unit, make_downtown_pie_chart, make_strathcona_pie_chart, 
make_fairview_pie_chart, areas):
    '''Function sub_charts_callback
       Input: functions, dicts, list
       Return: none

       Does: Initiates a TKinter window that takes in user input (mouse clicks)
       and presents pyplots accordingly
    '''
    root = Tk()
    root.title(ROOT_TITLE)
    root.geometry(ROOT_SIZE)
    frame1 = ttk.Frame(root)
    frame1.pack()
    frame2 = ttk.Frame(root)
    frame2.pack()

    frame1_title = ttk.Label(frame1, text = "Unit of Cultural Space per School Charts")
    frame1_title.pack()

    alphabetical = ttk.Button(frame1, text = "Bar Chart Sorted Alphabetically by Area Names", 
    command = lambda: make_bar_chart_by_area(dict_sort_by_area))
    alphabetical.pack()

    numerical = ttk.Button(frame1, text = "Bar Chart from Area with Most Cultural Space to Least", 
    command = lambda: make_bar_chart_by_unit(dict_sort_by_unit))
    numerical.pack()

    quit = ttk.Button(frame1, text = "Quit", command = root.destroy)
    quit.pack()

    frame2_title = ttk.Label(frame2, text = "Cultural Space Types Breakdown of Top 3 Areas")
    frame2_title.pack()

    downtown_pie = ttk.Button(frame2, text = "Downtown", command = lambda: make_downtown_pie_chart(areas))
    downtown_pie.pack()

    strathcona_pie = ttk.Button(frame2, text = "Strathcona", command = lambda: make_strathcona_pie_chart(areas))
    strathcona_pie.pack()

    fairview_pie = ttk.Button(frame2, text = "Fairview", command = lambda: make_fairview_pie_chart(areas))
    fairview_pie.pack()
    
    root.mainloop()

def main():

    try:
        school_data = open_csv("https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        school_name, school_coord, school_area = clean_school_data(school_data)
        schools = create_school_obj(school_name, school_coord, school_area)

        cultural_space_data = open_csv("https://opendata.vancouver.ca/explore/dataset/cultural-spaces/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord = clean_cultural_space_data(cultural_space_data)
        cultural_spaces = create_cultural_space_obj(cultural_space_name, cultural_space_type, cultural_space_area, cultural_space_coord)

        unique_areas = create_unique_area_list(school_area)
        areas = create_area_obj(unique_areas)
        analyze_school_cultural_space(areas, schools, cultural_spaces)

        school_cs_dict_sort_by_area = build_school_cs_dict_sort_by_area(areas)
        school_cs_dict_sort_by_unit = build_school_cs_dict_sort_by_units(areas)

        sub_charts_callback(make_school_cs_bar_chart_sort_by_area, make_school_cs_bar_chart_sort_by_unit,
        school_cs_dict_sort_by_area, school_cs_dict_sort_by_unit, make_downtown_pie_chart, make_strathcona_pie_chart,
        make_fairview_pie_chart, areas)
        
    except TypeError as ex:
        print("Invalid type:", ex)

if __name__ == "__main__":
    main()
