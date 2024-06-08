import string

h_name=input("Enter string\n")
if len(h_name)==0:
    exit()
h_name=h_name.lower().title()
h_name=h_name.replace(" ","")
for char in string.punctuation:
    h_name=h_name.replace(char, "")
h_name='#'+h_name[:139]
print(h_name)
print("length is ", len(h_name))

