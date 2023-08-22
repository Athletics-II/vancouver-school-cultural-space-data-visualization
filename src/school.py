'''
Siyi Ling
CS 5001, Fall 2022
Milestone 1

This is the School class file for school-cultural space analysis program.
'''

class School:
    '''
    Class: School
    It knows its own name, coordinates, and area, is equal to another instance
    if the two are in the same area.
    '''

    def __init__(self, name, coordinates, area):
        '''Constructor __init__
           Input: lst
           Returns: obj
        
           Does: instantiation
        '''
        self.name = name
        self.coordinates = coordinates
        self.area = area
    
    def __str__(self):
        '''Method __str__
           Input: none
           Return: str

           Does: defines the printed form of School obj
        '''
        printable = f"{self.name}"
        return printable
    
    def __eq__(self, other):
        '''Method __eq__
           Input: obj
           Return: bool

           Does: defines the = operator of School obj, raises ValueError as appropriate
        '''
        if type(other) != School:
            raise ValueError("Must compare two School objects.")
            
        if self.area == other.area:
            return True
        else:
            return False
    
    
