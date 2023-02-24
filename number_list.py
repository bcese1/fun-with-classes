num_list = []  # declares num_list as a list which is an object not a variable


class myNumberList:  # class myNumberList which adds and removes ints from a list. It will also return the head and the
    # list itself. The class itself is also callable.
    def __init__(self):  # initialize myNumberList and pass nothing to it
        None

    def add(self, value):  # function add which adds an int to a list
        if type(value) == int or type(value) == float:  # checks if value is type int or float
            num_list.append(value)  # if line 9 is true it will append the value into the list
            return num_list  # returns the list
        else:
            return 'Input is not an int'  # if the type of value is not int or float an error will print

    def remove(self, value):  # function remove which removes all occurrences of a value from a list
        if type(value) == int or type(value) == float:  # checks if value is type int or float
            num_list.remove(value)  # removes value from num_list if line 17 is true
            return num_list  # returns num_list
        else:
            return 'Input is not an int'  # else return this print error

    def head(self):  # function head will return the beginning of the list
        return num_list[0:1]  # return the beginning of the list using slicing

    def getList(self):  # function getList will return the list num_list
        return num_list  # returns num_list

    def __str__(self):  # function defines self as a string
        return str(num_list)  # returns the string of the num_list


class myRevOrderedNumberList(myNumberList):  # class myRevOrderedNumberList is a subclass of myNumberList which reverses
    # the list
    def __init__(self):  # initialize myRevOrderedNumberList and pass nothing to it
        None

    def head(self):  # function head will reverse the list and return it
        new_num_list = sorted(num_list, reverse=True)  # reverses the list
        return new_num_list[0:1]  # returns the first value of the list using slicing

    def getList(self):  # function getList will return the list
        return num_list  # returns list

# print statements test the different functions and class given by the specs
print(myNumberList().add(15.05))
print(myNumberList().add(15.06))
print(myNumberList().add('15.06'))
print(myNumberList().remove('15.05'))
print(myNumberList().head())
print(myNumberList().getList())
print(myNumberList().remove(15.05))
print(myNumberList())
print(myRevOrderedNumberList().add(15.05))
print(myRevOrderedNumberList().add(15.06))
print(myRevOrderedNumberList().add('15.05'))
print(myRevOrderedNumberList().remove('15.05'))
print(myRevOrderedNumberList().head())
print(myRevOrderedNumberList())
print(myRevOrderedNumberList().remove(15.05))