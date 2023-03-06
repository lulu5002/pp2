import re

string = 'HelloMyWorldOfPython'

words = re.findall('[A-Z][a-z]*', string)

print(' '.join((words)))