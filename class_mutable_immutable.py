'''
Is this Python Class mutable?
https://stackoverflow.com/questions/62029673/is-this-python-class-mutable
* use _ at the beginning of an attribute name indicating that it's not supposed to be accessed and/or modified by any code outside of the class.
* To access my_clock.time the interpreter needs to make some internal lookup of an attribute with the name time in a symbol table (just a fancy name for a dictionary) corresponding to the my_time object. 
* At the same time, when you are accessing the local variable a, a similar lookup is being performed in another symbol table (aka dictionary) corresponding to the current local scope.

@property Decorator 
https://www.freecodecamp.org/news/python-property-decorator/
'''

class Clock:
    def __init__(self, time):
        self._time = time   # non-public attribute/protected,  should not be accessed or modified directly outside of the class 
    @property           # == get time
    def time(self):
        return self._time
    
    @time.setter        # ==setter
    def time(self, value):
        self._time = value

    def print_time(self):
        print(self._time)


boston_clock = Clock('5:30')
paris_clock = boston_clock  # object reference, same object, one object
paris_clock.time = '10:30'  # update time
boston_clock.print_time()   # result is 5:30
print(id(paris_clock), id(boston_clock))    #same id
