''' Write a python function to remove a given word from a
    string and strip if at the same time '''

#strip :==> strip is a string function that remove given thing in a string

def remove_and_split(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()

this = "    This is not python    "
k = remove_and_split(this, "not ")
print(k)


