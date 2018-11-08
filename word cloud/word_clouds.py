import numpy as np
import pandas as pd
import random
from textblob import TextBlob

from wordcloud import WordCloud, STOPWORDS
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
import matplotlib.pyplot as plt
import re
import itertools

stopwords = set(STOPWORDS)


df=pd.read_csv("blog_content and titles.csv")


def preprocess_text(text):
  
  text = re.sub(r'@[a-zA-Z0-9]+','',text)
  text = re.sub(r"[^A-Za-z0-9]", " ", text)

  text = re.sub(r'  +',' ',text)
  
  return text


def tokenizer(text):
        tokens_ = [word_tokenize(sent) for sent in sent_tokenize(text)]
        
        tokens = []
        for token_by_sent in tokens_:
            tokens += token_by_sent
        tokens = [token for token in tokens if len(token) > 2]
        tokens = list(filter(lambda t: t.lower() not in stopwords, tokens))
        tokens = list(filter(lambda t: t not in punctuation, tokens))
        tokens = list(filter(lambda t: t not in [u"'s", u"n't", u"...", u"''", u'``', u"(",u")",u",",u"?"], tokens))
        return tokens

data=list(df['content'])
data=[preprocess_text(ix.lower()) for ix in data]
data=[tokenizer(ix.lower()) for ix in data]


data = list(itertools.chain(*data))
data = [w.replace('nbsp', '') for w in data]

# Replacing redundant / irrelevant words
words_to_replace=["thats","youre","dont","didnt","doesnt","know","ive"]
for word in words_to_replace:
    data = [w.replace(word, '') for w in data]

# print data
data= ' '.join(data)


#TextBlob tags : V- verb, N- noun, J- adjective
nouns=' '.join([w for (w, pos) in TextBlob(data).pos_tags if pos[0] == 'N'])
verbs=' '.join([w for (w, pos) in TextBlob(data).pos_tags if pos[0] == 'V'])
adjectives=' '.join([w for (w, pos) in TextBlob(data).pos_tags if pos[0] == 'J'])

def show_wordcloud(data, title = "Word Cloud for your WordPress Blog"):
    wordcloud = WordCloud(width=200, height=100,
        background_color='black',
        stopwords=stopwords,
        max_words=150, max_font_size=20,
                 scale=3, collocations=False,
        random_state=1 
    ).generate(nouns)


    fig = plt.figure(1, figsize=(50,30))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=6,bottom=1)
    plt.tight_layout(pad=10)

    #following line is for BLACK AND WHITE wordcloud
    plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
    plt.imshow(wordcloud)
    a=wordcloud.to_array()
    print a
    # print wordcloud.word_
    plt.show()

#FOr BLACK AND WHITE wordcloud
def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
show_wordcloud(data)
