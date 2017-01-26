from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('text8')
model = word2vec.Word2Vec(sentences, size=200)
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=2)
model.most_similar(['man'])
model.save('text8.model')
model.save_word2vec_format('text.model.bin', binary=True)
model1 = word2vec.Word2Vec.load_word2vec_format('text.model.bin', binary=True)
model1.most_similar(['girl', 'father'], ['boy'], topn=3)
more_examples = ["he is she", "big bigger bad", "going went being"]
for example in more_examples:
    a, b, x = example.split()
    predicted = model.most_similar([x, b], [a])[0][0]
    print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)
model_org = word2vec.Word2Vec.load_word2vec_format('/Users/hjp/MacBook/data/bin/text.bin', binary=True)
model_org.most_similar('frog')