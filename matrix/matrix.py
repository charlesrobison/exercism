import numpy


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        pass

    def row(self, index):
        stripped = self.matrix_string.replace(" ", "")
        my_list = [list(b) for b in stripped.splitlines()]
        y = numpy.array(my_list)
        return y[index]
        pass

    def column(self, index):
        stripped = self.matrix_string.replace(" ", "")
        my_list = [list(b) for b in stripped.splitlines()]
        y = numpy.array(my_list)
        return y[:, index]
        pass


# class Matrix:
#     def __init__(self, matrix_string):
#         self.matrix_string = matrix_string
#         stripped = matrix_string.replace(" ", "")
#         my_list = [list(b) for b in stripped.splitlines()]
#         y = numpy.array(my_list)
#         pass

#     def row(self, index):
#         return y[index]
#         pass

#     def column(self, index):
#         return y[:, index]
#         pass


# user_input = "1 2 3\n4 5 6\n7 8 9"
# edited = map(list, user_input.splitlines())

# for i in edited:
#     print(i)



# my_list = [list(b) for b in user_data.splitlines()]                     

# my_list                                                                 
# Out[7]: 
# [['1', ' ', '2', ' ', '3'],
#  ['4', ' ', '5', ' ', '6'],
#  ['7', ' ', '8', ' ', '9']]

# stripped = user_input.replace(" ", "")
# my_list = [list(b) for b in stripped.splitlines()]

# import numpy

# y = numpy.array(my_list)

# print(y[0])
# First row

# print(y[:, 0])
# First column
