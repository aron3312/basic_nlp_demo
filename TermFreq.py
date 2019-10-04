
def count_term_freq(text_file):
    with open(text_file, 'r', encoding='UTF-8') as f:
        all = []
        for text in f:
            all.extend(text.replace('\n', '').split(' '))
    all_voc = list(set(all))
    result = [(voc, all.count(voc)) for voc in all_voc]
    result = sorted(result, key=lambda x:-x[1])
    with open('example/term_freq.txt', 'w', encoding='utf-8') as term_freq:
        for r in result:
            term_freq.write('{} {}\n'.format(r[0], r[1]))


if __name__ == '__main__':
    count_term_freq('example/seg.txt')