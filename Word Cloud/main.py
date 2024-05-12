import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import PIL

text= 'Im Jay,I am developer'

wordcloud= WordCloud(width=800 , height=800).generate(text)

plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('Word Tree')
plt.show()
# save = 'wordcloud.png'
# wordcloud.to_file(save)