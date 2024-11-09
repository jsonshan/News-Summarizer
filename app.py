from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

from grab_news import *
from article_info import *

@app.route('/summary/<source>/<category>', methods=['GET'])
def index(source, category):
    # Use the passed title and category to grab article URLs
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

    # Get titles and summaries for the articles
    result = extract_valid_articles(article_urls)

    if len(result) == 2:
        titles, summaries = result

    return {"titles": titles, "summaries": summaries} # Return directly for testing purposes

if __name__ == '__main__':
    app.run(debug=True)
