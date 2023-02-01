######Classes

class MyClass:

    def __init__(self, x=0.):  #Constructor
        ######Define parameters to this class
        #Python will raise an error if x cannot be converted to a float
        self.x = x  
        self.name = 'an object of MyClass'

    #Restrict access to a private attribute
    #Allows python to see x as a public attribute
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        x = float(value)
        self._x = x

    def print_x(self):     ####Function in a Class if called a method
        print(f'x: {self.x}')
    
