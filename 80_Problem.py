''' Write a programe using function to find gretest 
    of three numbers '''

def maximum(num1,num2,num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
                return num3
    else:
            if (num2>num2):
                return num2
            else:
                return num3

m = maximum(32,43,66)
print("The value of the maximum number is " + str(m))
