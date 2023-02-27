'''
Is this Python Class mutable?
https://stackoverflow.com/questions/62029673/is-this-python-class-mutable

'''

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock  #object reference, same object, one object
paris_clock.time = '10:30'
boston_clock.print_time()   #result is 10:30
print(id(paris_clock), id(boston_clock))    #same id
