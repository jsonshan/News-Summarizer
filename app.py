from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# CNN News
def grab_urls_cnn(source_url):
    response = requests.get(source_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True, attrs={"data-link-type": "article"})
        article_urls = []
        for link in links:
            href = link['href']
            if href.startswith('/'):
                href = 'https://www.cnn.com' + href
            article_urls.append(href)
        return article_urls[:3]
    else:
        return []

# NBC News
def grab_urls_nbc(source_url):
    response = requests.get(source_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.findAll('h2', class_='multistoryline__headline')
        headlines += soup.findAll('h2', class_='styles_headline__ice3t')
        article_urls = []
        for headline in headlines:
            a_tag = headline.find('a', href=True)
            if a_tag:
                article_urls.append(a_tag['href'])
        return article_urls[:3]
    else:
        return []

# Time News
def grab_urls_time(source_url):
    response = requests.get(source_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_urls = []
        links = soup.find_all('a', href=True)
        for link in links:
            headline = link.find('h2', class_='headline')
            if headline:
                article_urls.append("https://time.com" + link['href'])
        return article_urls
    else:
        return []
    

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

        return article_urls
    else:
        print(f"Failed to retrieve {source_url}")
        return []

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

        return article_urls
    else:
        print(f"Failed to retrieve {source_url}")
        return []


def summarize_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs[:3]])  # Get first 3 paragraphs as summary
        return text
    return "Failed to retrieve article."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        source = request.form['source']
        if category == 'politics':
            sources = ['cnn', 'nbc', 'time', 'cbs', 'fox']  # All sources for politics
        else:
            sources = [source]  # Use only the selected source for other categories

        article_urls = []
        for s in sources:
            if s == 'cnn':
                article_urls += grab_urls_cnn(f"https://www.cnn.com/{category}")
            elif s == 'nbc':
                article_urls += grab_urls_nbc(f"https://www.nbcnews.com/{category}")
            elif s == 'time':
                article_urls += grab_urls_time(f"https://time.com/{category}")
            elif s == 'cbs':
                article_urls += grab_urls_cbs(f"https://www.cbsnews.com/{category}")
            elif s == 'fox':
                article_urls += grab_urls_fox(f"https://www.foxnews.com/{category}")

        article_urls = list(set(article_urls))  # Remove duplicates
        summaries = [summarize_article(url) for url in article_urls[:3]]  # Get summaries for top 3 articles
        
        return render_template('index.html', summaries=summaries, article_urls=article_urls[:3])

    return render_template('index.html', summaries=None)

if __name__ == '__main__':
    app.run(debug=True)
