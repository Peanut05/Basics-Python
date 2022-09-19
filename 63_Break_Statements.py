# break function :==>>
''' 'break'  is used to come out of the loop when 
    encountered it's instructs the programe the -exit
    from the loop now '''

for i in range(11):
    print(i)

    if i == 5: # break statement exit loop from value of i is 5
        break

# Else part is only executed after for loop is successfully terminated, or not.
else:
    print("for loop is executed")
