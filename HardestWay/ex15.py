from sys import argv

script, filename = argv
try:
    txt = open(filename)
except FileNotFoundError:
    with  open(filename, 'w') as txt:
        txt.write("""This is stuff I typed into a file.\n
        It is really cool stuff.\n
        Lots and lots of fun to have in here.""")

txt = open(filename)

print(f"Here is you file {filename}")
print(txt.read())

print('Type the filaname again:')
file_again = input('>')

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
