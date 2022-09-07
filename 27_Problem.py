''' Write a programe to accept marks of 8 students 
and and display them in a sorted manner '''


m1 = int(input("Enter marks of student number 1 :"))
m2 = int(input("Enter marks of student number 2 :"))
m3 = int(input("Enter marks of student number 3 :"))
m4 = int(input("Enter marks of student number 4 :"))
m5 = int(input("Enter marks of student number 5 :"))
m6 = int(input("Enter marks of student number 6 :"))
m7 = int(input("Enter marks of student number 7 :"))
m8 = int(input("Enter marks of student number 8 :"))

marks_list = [m1, m2, m3, m4, m5, m6, m7, m8]
marks_list.sort()
print(marks_list)
