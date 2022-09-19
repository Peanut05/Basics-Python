''' Write a program to print multiplication table of
    a given number using for loop '''

num = int(input("Enter a number for talbe : "))

for i in range(1 , 11):
    print(str(num) + "X" + str(i) + "=" + str(num*i) ) 

    # or :
    #print(f"{num}X{i}={num*i}") *f string


