from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

from grab_news import *
from article_info import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        source = request.form['source']

        article_urls = []
        if source == 'cnn':
            article_urls = grab_urls_cnn(f"https://www.cnn.com/{category}")
        elif source == 'nbc':
            article_urls = grab_urls_nbc(f"https://www.nbcnews.com/{category}")
        elif source == 'time':
            article_urls = grab_urls_time(f"https://time.com/{category}")
        elif source == 'cbs':
            article_urls = grab_urls_cbs(f"https://www.cbsnews.com/{category}")
        elif source == 'fox':
            article_urls = grab_urls_fox(f"https://www.foxnews.com/{category}")

        article_urls = list(set(article_urls))  # Remove duplicates
        
        # Get titles and summaries for the articles
        titles, summaries = extract_valid_articles(article_urls)

        return render_template('index.html', titles=titles, summaries=summaries, article_urls=article_urls)

    return render_template('index.html', titles=None, summaries=None)


if __name__ == '__main__':
    app.run(debug=True)
