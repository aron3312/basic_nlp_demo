import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pyLDAvis.gensim
import pyLDAvis

with open('example/seg.txt', 'r', encoding='utf-8') as f:
    all = []
    for p in f:
        all.append(p.replace('\n', '').split(' '))

id2word = corpora.Dictionary(all)

# Create Corpus

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in all]

# View


lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=3,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
print(lda_model.show_topics())
a = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
pyLDAvis.save_html(a, 'example/lda.html')