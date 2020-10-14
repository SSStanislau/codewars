'''
The collections module has defaultdict, which gives you a default value for trying to get the value of a key which does not exist in the dictionary instead of raising an error. Why not do this for a list?

Your job is to create a class (or a function which returns an object) called DefaultList. The class will have two parameters to be given: a list, and a default value. The list will obviously be the list that corresponds to that object. The default value will be returned any time an index of the list is called in the code that would normally raise an error (i.e. i > len(list) - 1 or i < -len(list)). This class must also support the regular list functions extend, append, insert, remove, and pop.

Because slicing a list never raises an error (slicing a list between two indexes that are not a part of the list returns [], slicing will not be tested for.

Example
lst = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
lst[4] = True
lst[80] = 'default_value'
lst.extend([104, 1044, 4066, -2])
lst[9] = -2
'''


class DefaultList:
    def __init__(self, *args):
        self.arr = args[0]
        self.default = args[1]
    
    def __getitem__(self, key):
        return self.default if key > len(self.arr) - 1 or key < -len(self.arr) else self.arr[key]
    
    def extend(self, array):
        self.arr.extend(array)
    
    def append(self, value):
        self.arr.append(value)
        
    def remove(self, key):
        self.arr.remove(key)
    
    def pop(self, key):
        self.arr.pop(key)
    
    def insert(self, i, el):
        self.arr.insert(i, el)
