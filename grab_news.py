import requests
from bs4 import BeautifulSoup
from model import generate_summary
import re


# CNN News

def grab_urls_cnn(source_url):
    # Send a GET request to the category URL
    response = requests.get(source_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags with href and specific data-link-type attributes
        links = soup.find_all('a', href=True, attrs={"data-link-type": "article"})

        # Collect the article URLs
        article_urls = []

        for link in links:
            href = link['href']
            # Make sure the URL is absolute
            if href.startswith('/'):
                href = 'https://www.cnn.com' + href
            article_urls.append(href)

        # Return the top 3 article URLs
        return article_urls[:3]
    else:
        print(f"Failed to retrieve {source_url}")
        return []


# NBC News


def grab_urls_nbc(source_url):
    # Send a GET request to the category URL
    response = requests.get(source_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <h2> tags with the specified class name
        headlines = soup.findAll('h2', class_='multistoryline__headline')
        headlines += soup.findAll('h2', class_='styles_headline__ice3t')
        # Collect the article URLs
        article_urls = []
        
        for headline in headlines:
            # Look for <a> tags within each <h2> element and get their href attribute
            a_tag = headline.find('a', href=True)
            if a_tag:
                article_urls.append(a_tag['href'])

        # Return the top 3 article URLs
        return article_urls[:3]
    else:
        print(f"Failed to retrieve {source_url}")
        return []


# time news

def grab_urls_time(source_url):
    # Send a GET request to the category URL
    response = requests.get(source_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Collect the article URLs where <a> tags contain an <h2> tag with class 'headline'
        article_urls = []

        # Find all <a> tags on the page
        links = soup.find_all('a', href=True)
        
        for link in links:
            # Check if the <a> tag contains an <h2> tag with class 'headline'
            headline = link.find('h2', class_='headline')
            if headline:
                article_urls.append("https://time.com" + link['href'])

        return article_urls[:3]
    else:
        print(f"Failed to retrieve {source_url}")
        return []


# CBS news

def grab_urls_cbs(source_url):
    # Send a GET request to the category URL
    response = requests.get(source_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Collect the article URLs where <article> contains an <a> tag
        article_urls = []

        # Find all <article> tags with the specific class that CBS uses
        articles = soup.find_all('article', class_='item')

        for article in articles:
            # Find the <a> tag within each <article> tag
            link = article.find('a', href=True)
            if link:
                article_urls.append(link['href'])

        return article_urls[:3]
    else:
        print(f"Failed to retrieve {source_url}")
        return []


# Fox news

def grab_urls_fox(source_url):
    # Send a GET request to the category URL
    response = requests.get(source_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Collect the article URLs where <article> contains an <a> tag
        article_urls = []

        # Find all <article> tags with the specific class that CBS uses
        articles = soup.find_all('article', class_='article')

        for article in articles:
            # Find the <a> tag within each <article> tag
            link = article.find('a', href=True)
            if link:
                article_urls.append('https://foxnews.com' + link['href'])

        return article_urls[:3]
    else:
        print(f"Failed to retrieve {source_url}")
        return []
