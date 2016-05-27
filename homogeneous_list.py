#######################################################################
                             #Demo

#>>>from homogeneous_list import *
#>>>MyList.acceptonly('int')
#>>>int_list = MyList()
#>>>int_list.append(1)

#>>>int_list.append(2)

#>>>int_list.append(3)

#>>>int_list
#>>>[1,2,3]

#>>>int_list.append(3.0)
#>>>OOPS!!!!! Sorry you can't append differnt data_type value in this list


#>>>MyList.acceptonly('str')
#>>>str_list = MyList()
#>>>str_list.append('Hi')

#>>>str_list.append('How are you')

#>>>str_list.append('Thanks')

#>>>str_list
#>>>['Hi','How are you','Thanks']

#>>>str_list.append(11100)
#>>>OOPS!!!!! Sorry you can't append differnt data_type value in this list

#######################################################################


data_type_dict = {'int': int, 'str': str, 'float': float}  # data_type_dict to check the user value 


def decorator(orig_func):
    def wrap_func(self, *args):
        if orig_func.__name__ == 'append':
            args = [args, ]            
        for arg in args[0]:
            if self.data_type == type(arg) or not self.data_type:
                '''
                   check if the user value's datatype is same as MyList datatype
                   or the MyList datatype is None
                '''
                if orig_func.__name__ == 'extend':
                    orig_func(self, [arg])
                else:
                    orig_func(self, arg)
            else:
                print("OOPS!!!!! Sorry you can't append '%s' (differnt data type) value in this list" %(arg))
    return wrap_func


class MyList(list):
    data_type = None  # If data_type is None, List will accept all data_type 

    def __init__(self, *args, **kwargs):
        '''save the class's date_type to self object'''
        self.data_type = MyList.data_type
        super(MyList, self).__init__(*args, **kwargs)

    @classmethod
    def acceptonly(cls, data_type):
        '''class method to accept the datatype from user for the list object'''
        cls.data_type = data_type_dict[data_type]

    @decorator
    def append(self, val):
        '''append a value which has the same data type of the MyList class'''
        super(MyList, self).append(val)

    @decorator
    def extend(self, *val_list):
        '''append a value which has the same data type of the MyList class'''
        super(MyList, self).extend(*val_list)

    def insert(self, index, val):
        '''insert the value which has the same data type of the MyList's data_type '''
        if self.data_type == type(val) or not self.data_type:
            super(MyList, self).extend(index, val)
        else:
            print("OOPS!!!!! Sorry you can't append '%s' (differnt data type) value in this list" %(val))
                
