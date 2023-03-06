import re
text = "PythonSplittingWithRegex"
print(re.findall('[A-Z][^A-Z]*', text))
