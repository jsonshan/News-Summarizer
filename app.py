from flask import Flask, render_template, request
import requests
from flask_cors import CORS
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)

from grab_news import *
from article_info import *

@app.route('/summary/<source>/<category>', methods=['GET'])
def index(source, category):
    cnn_cat_urls = { 
    'world': 'https://www.cnn.com/world', 
    'business': 'https://www.reuters.com/business/', 
    'technology': 'https://www.cnn.com/business/tech', 
    'entertainment': 'https://www.cnn.com/entertainment', 
    'politics': 'https://www.cnn.com/politics', 
    'sports': 'https://www.cnn.com/sport' 
    }

    nbc_cat_urls = { 
        'world': 'https://www.nbcnews.com/world', 
        'business': 'https://www.nbcnews.com/business', 
        'technology': 'https://www.nbcnews.com/tech-media', 
        'politics': 'https://www.nbcnews.com/politics', 
        'sports': 'https://www.nbcnews.com/sports' 
    }

    time_cat_urls = { 
        'world': 'https://time.com/section/world/', 
        'business': 'https://time.com/section/world/', 
        'technology': 'https://time.com/section/tech/', 
        'entertainment': 'https://time.com/section/entertainment/', 
        'politics': 'https://time.com/section/politics/', 
        'sports': 'https://time.com/section/sports/' 
    }

    cbs_cat_urls = { 
    'world': 'https://www.cbsnews.com/world/', 
    'finance': 'https://www.cbsnews.com/moneywatch/', 
    'business': 'https://www.cbsnews.com/evening-news/business/', 
    'technology': 'https://www.cbsnews.com/technology/', 
    'entertainment': 'https://www.cbsnews.com/entertainment/', 
    'politics': 'https://www.cbsnews.com/politics/', 
    'sports': 'https://www.cbssports.com/' 
    }

    fox_cat_urls = { 
        'world': 'https://www.foxnews.com/world', 
        'finance': 'https://www.foxbusiness.com/economy', 
        'business': 'https://www.foxbusiness.com/', 
        'technology': 'https://www.foxnews.com/category/tech/artificial-intelligence', 
        'entertainment': 'https://www.foxnews.com/entertainment', 
        'politics': 'https://www.foxnews.com/politics', 
        'sports': 'https://www.foxnews.com/sports' 
    }

    # Use the passed title and category to grab article URLs
    article_urls = []
    if source == 'cnn':
        if category in cnn_cat_urls:
            article_urls = grab_urls_cnn(cnn_cat_urls[category])
    elif source == 'nbc':
        cat_url = nbc_cat_urls[category]
        if category in nbc_cat_urls:
            article_urls = grab_urls_nbc(nbc_cat_urls[category])
    elif source == 'time':
        if category in time_cat_urls:
            article_urls = grab_urls_time(time_cat_urls[category])
    elif source == 'cbs':
        if category in cbs_cat_urls:
            article_urls = grab_urls_cbs(cbs_cat_urls[category])
    elif source == 'fox':
        if category in fox_cat_urls:
            article_urls = grab_urls_fox(fox_cat_urls[category])

    # Get titles and summaries for the articles
    result = extract_valid_articles(article_urls)

    if len(result) == 2:
        titles, summaries = result

    return {"titles": titles, "summaries": summaries} # Return directly for testing purposes

if __name__ == '__main__':
    app.run(debug=True)
