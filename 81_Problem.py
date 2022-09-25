''' Write a python progame using function to convert
    celsius to fahrenheit (get formula from google)'''

def fahre(cel):
    return (cel * (9/5)) + 32

c = 45
f = fahre(c)
print("fahrenheit is :" + str(f))
