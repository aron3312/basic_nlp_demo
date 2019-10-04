import jieba

with open('example/raw_data.txt', 'r', encoding='UTF-8') as f:
    with open('example/seg.txt', 'w', encoding='utf-8') as out:
        for text in f:
            out.write('{}\n'.format(' '.join([p for p in jieba.cut(text)]).replace('\n', '')))
