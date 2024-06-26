def popular_words (text, words):
    text_split = text.lower().split()
    res = dict.fromkeys(words, 0)
    for word_ in text_split:
        if word_ in words:
            res[word_] = res.get(word_,0)+1
    return res

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
