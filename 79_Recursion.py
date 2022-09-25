# Recursion :==>>
''' Recursion is a function which calls itself.
    it is used to directly use a mathamathical formula 
    as a fuction.
    example :----  
                    factorial(n)=n*factorial(n-1)'''

''' The parameter need to extremely careful while working with recursion
    to ensure that the function dosen't infinitely keep calling itself
    recursion is sometimes the most direct way to code an algorithem '''
    
# example.:---

'''n = 0  #number that input for factorial
product = 0
for i in range(n):
    product = product * (i+1)
print(product)'''

'''n = 2
product = 1
for i in range(n):
    product = product * (i+1)
print(product)'''

'''def fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
f = fact(5)
print(f)'''

# using Recursion:===>>>

def fact_recursive(n):
    if n==1 or n==0:   #formula                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        return 1
    return fact_recursive(n-1) *n
f = fact_recursive(2) #Function calling itself and got all metod in duntion

print(f)




