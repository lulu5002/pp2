def is_palindrome(string):
    return string == ''.join(reversed(string))

string = input("Enter your word:")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")