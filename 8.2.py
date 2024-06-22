import string

def is_palindrome(text):
    text_processed = ''.join(x.lower() for x in text if not x in string.punctuation+' ')
    return text_processed==text_processed[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")