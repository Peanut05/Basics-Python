''' Write a programe to find the given username is contains 
    less than 10 charecters or not'''

usuername = input("Enter username : ")

length = len(usuername)

if(length < 10):
    print("Username is less than 10 charecters ")

else:
    print("Username is greter than 10 charecters ")

print("usename contain" + str(length)+ "charecters ")
