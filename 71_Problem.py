''' Write a programe to calculate factorial of a
    given number using for loop '''

# n! = 1*2*3*4*5*6*7.....*n factorial of number

num = int(input("Enter number for factorial : "))
factorial = 1
for i in range(num,num+1):
    factorial = factorial * i

print(f"factorial of {num} is {factorial} ")
