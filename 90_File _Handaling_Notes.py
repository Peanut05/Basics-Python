Python File Handling
File handling in python lets you open, read, write, append, modify files.

Note: For the sake of this tutorial, we will assume that your text file and python code are present in the same directory.

Before we perform any operation on file, we need to open the file. This is done using the open() function.

 

Example: lets say we have a text file (someText.txt) with some content in it. The open() function creates a file object with read() method for reading the content.

file = open("someText.txt")
print(file.read())
Output:

lorem ipsum

In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.
 

There are various modes in which we can open files.

read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
create (x): This mode creates a file and gives an error if the file already exists.
 

Apart from these modes we also need to specify how the file must be handled:

text (t): Used to handle text files.
binary (b): used to handle binary files (images).
