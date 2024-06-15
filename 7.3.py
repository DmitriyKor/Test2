def second_index(text, some_str):
    pos=text.find(some_str)
    if pos>-1:
        pos=text.find(some_str, pos+1, len(text))
    if pos==-1:
        pos=None
    return(pos)

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')