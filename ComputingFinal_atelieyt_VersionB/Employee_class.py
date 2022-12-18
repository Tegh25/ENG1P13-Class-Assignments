'''
Teghveer Ateliey
atelieyt
400409275
Version B
April 7, 2022
'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    #### Accessor Methods ####
    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    #### Mutator Methods ####
    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.salary = salary
