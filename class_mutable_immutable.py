'''
Is this Python Class mutable?
https://stackoverflow.com/questions/62029673/is-this-python-class-mutable
* use _ at the beginning of an attribute name indicating that it's not supposed to be accessed and/or modified by any code outside of the class.
* To access my_clock.time the interpreter needs to make some internal lookup of an attribute with the name time in a symbol table (just a fancy name for a dictionary) corresponding to the my_time object. 
* At the same time, when you are accessing the local variable a, a similar lookup is being performed in another symbol table (aka dictionary) corresponding to the current local scope.
'''

class Clock:
    def __init__(self, time):
        self._time = time   
    def time(self):
        return self._time

    def print_time(self):
        print(self._time)

boston_clock = Clock('5:30')
paris_clock = boston_clock  # object reference, same object, one object
paris_clock.time = '10:30'  # ??? assign value to a function?
boston_clock.print_time()   # result is 5:30
print(id(paris_clock), id(boston_clock))    #same id
