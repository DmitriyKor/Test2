import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html =  file.read()
        res=''
        cur_pos=0
        prev_pos=0
        while cur_pos<len(html):
            cur_pos=html.find('<', cur_pos)
            if (cur_pos==-1):
                break
            res=res + html[prev_pos:cur_pos]
                #prev_pos=cur_pos + 1
            cur_pos=html.find('>', cur_pos)
            if (cur_pos==-1):
                break
            cur_pos+=1
            prev_pos=cur_pos
        file.close()
    if len(res)>0:
        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(res)
            file.close()

delete_html_tags('C:/Users/Public/Documents/draft.html', 'C:/Users/Public/Documents/cleaned.txt7')