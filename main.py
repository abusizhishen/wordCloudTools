import jieba
import os
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud

from os import path
from wordcloud import WordCloud
# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'text.txt')).read()
# Read the whole text.
# Generate a word cloud image
font = r'./msyh.ttf'
word_list = [" ".join(jieba.cut(sentence)) for sentence in [text]]
new_text = ' '.join(word_list)
wordcloud = WordCloud(font_path=font, width=800, height=800, max_font_size=40,
                      random_state=42, max_words=100).generate(new_text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("%s.png" % id)