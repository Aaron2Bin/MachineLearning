from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread

text = open('song.txt', 'r').read()
mask_img = imread('mask.png')
stopwd = ['is', 'a', 'the', 'to', 'of', 'in', 'on', 'at', 'and']
wdcd = WordCloud(mask=mask_img, background_color='white', scale=1.5, stopwords=stopwd)
wdcd = wdcd.generate(text)
plt.imshow(wdcd)
plt.axis('off')
plt.show()
wdcd.to_file('result.jpg')