def popular_words (text, words):
    text_split = text.lower().split()
    res = dict.fromkeys(words, 0)
    for word_ in words:
        if word_ in text_split:
            res[word_] = text_split.count(word_)
    return res

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
