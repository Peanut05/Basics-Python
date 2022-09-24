# A function is a group of statements performing a specific task
''' When a programe gets bigger in size and it's coplaxity grows,
    it get difficult for programmer to keep trck on which pieace of code is
        doing what '''

''' a function ca be reuse by programmer in a given programe 
    any number of time'''

# syntax of function :--->>
                    '''  def function():
                            print("Hello world") 

            this functio can be called any number of times, anywhere in the programe'''

# call Function:---->
    ''' whenever we want to call a function, we put the name of a function 
        followed by parantheisis as follows :

                                    function() ===>> function called in programe '''

# Function defination :==>>
''' The part containing the exact set of instructions
    which are exeucted during the function call (write in it is function def)'''

# Example to calculate persantage of student using function 

def persent (marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1 = [70,60,78,68]
persantage1 = persent(marks1)

marks2 = [80,88,90,87]
persantage2 = persent(marks2)

print(persantage1,persantage2)






