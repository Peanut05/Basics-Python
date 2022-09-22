''' Write a programe to print multiplication table 
    of n using for loop in reversed order '''

num = int(input("Enter number to print table in reverce order : "))

n = 11
for i in range (n,1):
    tb = num * i
    print(tb)
