''' A spam comment is defined as a text containing following rewords
    "make a lot of money" , "buy now" , "subscribe this" , "click this"
    write a programe to detect this spam '''

# Spam text detector :==>>
text = input("Enter the text : ")

if("make a lot of momey" in text):
    spam = True

elif("buy now" in text):
    spam = True

elif("subscribe this" in text):
    spam = True

elif("click this" in text):
    spam = True

else:
    spam = False

if(spam == True):
    print("Text is spam ")

else:
    print("Text is not spam ")
