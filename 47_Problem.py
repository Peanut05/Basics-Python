''' Write a programe to find out the greatest of four
    number entered by the user '''

n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
n3 = int(input("Enter number 3 :"))
n4 = int(input("Enter number 4 :"))

if(n1>n4):
    g1 = n1
else:
    g1 = n4

if(n2>n3):
    g2 = n2
else:
    g2 = n3

if(g1>g2):
    print(str(g1) + " Is gretest !")
else:
    print(str(g2) + " Is gretest !")
