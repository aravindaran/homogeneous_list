# homogeneous_list 

This package is written in python. 

Custom list class  in python which accept the given data type (Eg:Integer or float)

and also implement all the common function of list like append, extend, insert, pop . If user

gives any other data type it won't not accept and pop up an error.

Eg1:
>>>from homogeneous_list import *

>>>MyList.acceptonly('int') #it will accept integers only

>>>new_list = MyList()

>>>new_list.append(5) # it will produce output

>>>new_list.append(5.0) # it will produce an error

>>>OOPS!!!!! Sorry you can't append differnt data_type value in this list

Eg2: 
>>>MyList.acceptonly('str')

>>>str_list = MyList()

>>>str_list.append('Hi')

>>>str_list.append('How are you')

>>>str_list.append('Thanks')

>>>str_list

>>>['Hi','How are you','Thanks']

>>>str_list.append(11100)

>>>OOPS!!!!! Sorry you can't append differnt data_type value in this list

