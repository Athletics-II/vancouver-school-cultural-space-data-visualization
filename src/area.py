'''
Siyi Ling
CS 5001, Fall 2022
Milestone 1

This is the Area class file for school-cultural space analysis program.
'''

class Area:
    '''
    Class: Area.
    It knows its own name, is equal to another instance if the two have same names, 
    can update schools, cultural spaces, and cultural space types, and count cultural 
    spaces and types per school.
    '''

    def __init__(self, name):
        '''Constructor __init__
           Input: lst
           Returns: obj
        
           Does: instantiation
        '''
        self.name = name
        self.school_list = []
        self.cultural_space_list = []
        self.cultural_space_per_school = 0
        self.cultural_space_type_dict = {}
        self.cultural_space_type_per_school = {}
    
    def __str__(self):
        '''Method __str__
           Input: none
           Return: str

           Does: defines the printed form of Area obj
        '''
        printable = f"{self.name}"
        return printable

    def __eq__(self, other):
        '''Method __eq__
           Input: obj
           Return: bool

           Does: defines the = operator of Area obj, raises ValueError as appropriate
        '''
        if type(other) != Area:
            raise ValueError("Must compare two Area objects.")

        if self.name == other.name:
            return True
        else:
            return False
    
    def update_school_list(self, schools):
        '''Method update_school_list
           Input: list
           Return: none

           Does: updates school list with all schools in one area
        '''
        for school in schools:
            if school.area == self.name:
                self.school_list.append(school)
    
    def update_cultural_space_list(self, cultural_spaces):
        '''Method update_cultural_space_list
           Input: list
           Return: none

           Does: updates cultural space list with all cultural spaces in one area
        '''
        for space in cultural_spaces:
            if space.area == self.name:
                self.cultural_space_list.append(space)
    
    def count_cultural_space_per_school(self):
        '''Method count_cultural_space_per_school
           Input: none
           Return: none

           Does: count unit of cultural space per school in one area
        '''
        self.cultural_space_per_school = round(len(self.cultural_space_list) / len(self.school_list), 1)
    
    def update_cultural_space_type_dict(self):
        '''Method update_cultural_space_type_list
           Input: none
           Return: none

           Does: updates school list with all cultural space types in one area
        '''
        for space in self.cultural_space_list:
            if space.type not in self.cultural_space_type_dict.keys():
                self.cultural_space_type_dict[space.type] = 1
            else:
                self.cultural_space_type_dict[space.type] += 1
    
    def count_cultural_space_type_per_school(self):
        '''Method ount_cultural_space_type_per_school
           Input: none
           Return: none

           Does: count unit of cultural space type per school in one area
        '''
        if len(self.cultural_space_list) == 0.0:
            self.cultural_space_type_per_school["Any type"] = "None"
        else:
            for type in self.cultural_space_type_dict.keys():
                self.cultural_space_type_per_school[type] = round(self.cultural_space_type_dict[type] / len(self.school_list), 1)
        
        
