"""
Example classes
"""

class ParentClassOne(object):

    count = 0

    # When class instance is created
    def __init__(self):
        # Calls the next __init__ in the chain
        super().__init__()

        # Run method and assign instance variable
        self.count_add()
        self.instance_variable = "Instance variable"

    # When class instance is deleted or garbage collected
    def __del__(self):
        self.count_remove()

    # Used for print, if not existing __repr__ is used instead
    def __str__(self):
        return "Object string"

    # The object representation, usually unambigious
    def __repr__(self):
        return "Object representation"

    # Return an object with a next() method for iteration
    def __iter__(self):
        return self

    # next() method for iterator
    def next(self):
        return self

    # Staticmethod removes the requirement for self argument
    @staticmethod
    def static_test():
        return "Test static method"

    # Classmethod removes the requirement for self, but requires cls
    @classmethod
    def count_remove(cls):
        cls.count -= 1

    @classmethod
    def count_add(cls):
        cls.count += 1

class ParentClassTwo(object):

    def __init__(self):
        self.instance_variable_2 = "Instance variable two"

class ChildClass(ParentClassOne, ParentClassTwo):

    def __init__(self):
        # Calls ParentClassOne __init__
        super().__init__()


"""
Test example classes
"""

# Only run if file is being run directly
if __name__ == "__main__":

    # Creating objects
    object1 = ParentClassOne()
    print(object1.count)
    object2 = ChildClass()
    print(object2.count)

    # Print instance variables
    print(object1.instance_variable)
    print(object2.instance_variable)
    print(object2.instance_variable_2)

    # Change instance variable
    object1.instance_variable = "Instance variable changed 1"
    print(object1.instance_variable)
    print(object2.instance_variable)

    # Print count
    print(object1.count)
    print(object2.count)

    # Delete object
    del object1

    # Print count
    print(object2.count)

    # Print representation
    print(object2)

    # Print static method
    print(object2.static_test())
