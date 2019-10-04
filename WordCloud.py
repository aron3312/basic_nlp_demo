from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

font_path = 'C:/Windows/Fonts/kaiu.ttf'
wc = WordCloud(font_path=font_path, background_color="white", max_words=200,
               max_font_size=100, random_state=42, width=500, height=500, margin=2,)

with open('example/seg.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')
wc.generate(text)

#
# with open('example/term_freq.txt', 'r', encoding='utf-8') as f:
#     all = []
#     for p in f:
#         all.append((p.replace('\n', '').split(' ')[0], int(p.replace('\n', '').split(' ')[1])))
#
# all = [p for p in all if p[1] > 5]
# wc.generate_from_frequencies(dict(all))

plt.figure()
# recolor wordcloud and show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file('example/wordcloud.png')