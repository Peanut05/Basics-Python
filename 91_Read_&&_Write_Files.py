Read/Write Files
A. Create a File:
Creating a file is primarily done using the create (x) mode.

Example:

file = open("Text.txt", "x")
Output:

A file named Text.txt is created with no content.
 

B. Write onto a File:
This method writes content onto a file.

Example:

file = open("Text.txt", "w")
file.write("This is an example of file creation.")
file.close
Output:

This is an example of file creation.
 

If the file already exists with some content of its own, then this mode overwrites it.

Example:

file = open("Text.txt", "w")
file.write("This is overwritten text.")
file.close
Output:

This is overwritten text.
 

C. Read a File:
This method allows us to read the contents of the file.

Example:

file = open("Text2.txt", "r")
print(file.read())
file.close
Output:

Hello, I’m a Potato.
 

D. Append a File:
This method appends content into a file.

Example:

file = open("newText.txt", "a")
file.write("This is an example of file appending.")
file.close
Output:

This is an example of file appending.
 

However, If the file exists already with some content in it, then the new content gets appended.

Example:

file = open("newText.txt", "a")
file.write(" Hello, I'm appending")
file.close
Output:

This is an example of file appending. Hello, I'm appending
