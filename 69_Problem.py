''' Write program a find out the given number is prime or not'''

num = int(input("Enter Number For check primr or not"))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
    break
if prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

