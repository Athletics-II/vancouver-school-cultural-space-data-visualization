'''
Siyi Ling
CS 5001, Fall 2022
Milestone 1

This is the CulturalSpace class file for school-cultural space analysis program.
'''

class CulturalSpace:
    '''
    Class: CulturalSpace
    It knows its own name, type, area, and coordinates, is equal to another instance 
    if the two are in the same area.
    '''

    def __init__(self, name, type, area, coordinates):
        '''Constructor __init__
           Input: lst
           Returns: obj
        
           Does: instantiation
        '''
        self.name = name
        self.type = type
        self.area = area
        self.coordinates = coordinates
        
    def __str__(self):
        '''Method __str__
           Input: none
           Return: str

           Does: defines the printed form of CulturalSpace obj
        '''
        printable = f"{self.name}"
        return printable
    
    def __eq__(self, other):
        '''Method __eq__
           Input: obj
           Return: bool

           Does: defines the = operator of CulturalSpace obj, raises ValueError as appropriate
        '''
        if type(other) != CulturalSpace:
            raise ValueError("Must compare two CulturalSpace objects.")

        if self.area == other.area:
            return True
        else:
            return False
