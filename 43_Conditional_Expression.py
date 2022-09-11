# Conditional Expression :--->

''' 1) when today is sunday , I will play vedio games.
    2) I want to go goa , after parents permission.
    3) when bus is not avilable , I will go from train. 
    4) If i will pass i'm happy else sad '''

''' There are all of the above are decissions which
    depends on a condition being met '''

''' In python programming too, we must be able to create 
    instructions on a condition being met then thats executes
    or negitive part of a conditon will be executue '''

# If else and elif statement in python :-------->
''' if else and elif statements in python are a multiway disission
    taken by our programe due to cirtain conditions in our code '''

# Syntax :--->
''' if (condition 1):  *executes if condition 1 is true
        print("True")
    elif(condition 2): **executes if condition 2 is true
        print("False")
    else:               *** otherwise that part executes 
        print("True/false") '''

# 1) If , elif and else ladder in python :------>
# ladder means its only checkout one true condition and it exit from it
# that type of ladder will stop once a condition in an if or elif is met ;)
# imp::==>> 1)There can be any number of elif ststements .
           #3)Last else will be exectutes when all if and elif conditions get fail.
           #4) Else is actually optional. if you need then you can use it.
a = 6
if(a>9):
    print("a is greter than 9")
elif(a>5):
    print("a is greter than 5")
elif(a>11):
    print("a is greter than 11")
else:
    print("a is less than all numbers")
print("Done")

# 2) Multipal if statement :---->
# mutipal if statements are used for check every condition in a programe .
# it's check out every if conditions in a programe then it exit of it.

b = 5
if (b<9):
    print("b is less than 9")

if (b<7):
      print("b is less than 7")

if (b<12):
    print("b is less than 12")

else:
    print("b is greter than overall number")
print("Done")

