''' Write a program to print table of given nummber 
    using while loop with write seprate formula for 
    table '''

num = int(input("Enter number for table : "))
i = 1
while (i<=10):
    table = num * i # formula for table
    print(str(num) + "X" + str(i) + "=" + str(table))
    i = i + 1

