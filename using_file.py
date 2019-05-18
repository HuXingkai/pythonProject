poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
filename='usingFile.txt'

with open(filename,'a') as file_object:
    file_object.write('I also love java\n')
    file_object.write('I love creating\n')

