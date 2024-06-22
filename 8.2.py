import string

def is_palindrome(text):
    left_to_right = ''.join(x.lower() for x in text if not x in string.punctuation+' ')
    right_to_left = left_to_right[::-1]
    return left_to_right==right_to_left

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")