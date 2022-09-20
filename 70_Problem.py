''' Write a programe to find uot the sum of
    first n natural numbers using while loop '''

num = int(input("Enter the number till calculate numbers"))
add = 0
for i in range (1 , num+1):
    add = add + i
    i = i + 1

print("natural number sum till",add)
