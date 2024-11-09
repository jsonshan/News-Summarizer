from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

from grab_news import *
from article_info import *

@app.route('/', methods=['GET', 'POST'])
def index(title, category):
    # Use the passed title and category to grab article URLs
    article_urls = []
    if title == 'cnn':
        article_urls = grab_urls_cnn(f"https://www.cnn.com/{category}")
    elif title == 'nbc':
        article_urls = grab_urls_nbc(f"https://www.nbcnews.com/{category}")
    elif title == 'time':
        article_urls = grab_urls_time(f"https://time.com/{category}")
    elif title == 'cbs':
        article_urls = grab_urls_cbs(f"https://www.cbsnews.com/{category}")
    elif title == 'fox':
        article_urls = grab_urls_fox(f"https://www.foxnews.com/{category}")

    article_urls = list(set(article_urls))  # Remove duplicates

    # Get titles and summaries for the articles
    titles, summaries = extract_valid_articles(article_urls)

    return titles, summaries  # Return directly for testing purposes

if __name__ == '__main__':
    app.run(debug=True)
