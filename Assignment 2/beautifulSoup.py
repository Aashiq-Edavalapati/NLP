import bs4 as bs
import urllib.request
import re
import nltk

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article, 'html')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

processed_article = article_text.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article)
processed_article = re.sub(r'\s+', ' ', processed_article)
