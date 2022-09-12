''' Write a program to find out a student is pass or fail.
    if it erquires total 40% and at least 33% in each subject to pass,
    Assume 3 subjects and take marks as an input form the user. '''
   
sub1 = int(input("Enter your marks of first subject : "))
sub2 = int(input("Enter your marks of second subject : "))
sub3 = int(input("Enter your marks of third subject : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("\nyou are fail due to you have less than 33 in some sublect")
if(sub1+sub2+sub3)/3 <40 :
    print("\nYou are fail due to you have less than 40% ")
else:
    print("Congrats You are pass! ")
