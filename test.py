from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# These are the methods you import (grab_news and article_info)
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


def test_index_function():
    # Example: Test with 'time' as the source and 'politics' as the category
    title = 'time'
    category = 'politics'
    
    titles, summaries = index(title, category)  # Pass title and category

    # Check the results (assuming there should be at least 3 titles and summaries)
    print("Test Case Result:")
    print("Titles:", titles[1])  # Print the first 3 titles
    print("Summaries:", summaries[1])  # Print the first 3 summaries


if __name__ == '__main__':
    test_index_function()  # Run the test case directly
