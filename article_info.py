import requests
from google.generativeai import genai
from bs4 import BeautifulSoup

from model import generate_summary

instruction_category = {
    "You are a web scraping and article categorization expert specializing in identifying and classifying articles from a list of URLs. " \
    "When I provide a URL, extract all hyperlinks that are likely to be articles based on the presence of the year '2024' in the URL or content. " \
    "Further narrow down by filtering out links that are not news, articles, or stories by checking for relevant keywords ('news', 'article', 'story', etc.). " \
    "Classify any extracted articles into the following categories: 'World', 'Finance', 'Business', 'Technology', 'Pop Culture', 'Entertainment', 'Politics', 'Sports', or 'Other' based on their content. " \
    "Do not provide explanations. Return the article title and summary."
}

model_category = genai.GenerativeModel("models/gemini-1.5-flash", system_instruction=instruction_category)

def extract_valid_articles(article_urls):

    # Initialize lists to store the results
    title_list = []
    summary_list = []

    for url in article_urls:
        try:
            # Extract title and summary using the generative model
            result = model_category.generate_content([url])

            # Extract title from the model response
            title = result.text.split("\n")[1].replace("Title: ", "").strip()

            # Fetch and process the full article text from the URL
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Try to find main article content, adjust based on actual website structure
            article_body = soup.find('div', class_='article-body')  # Modify this if needed
            if not article_body:
                article_body = soup  # Fallback if specific tag not found
            
            paragraphs = article_body.find_all('p')
            article_text = ' '.join(para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True))
            article_text = ' '.join(article_text.split())  # Clean up excessive whitespace
            
            # Generate summary using the article text
            summary = generate_summary(article_text)

            # Append to respective lists
            title_list.append(title)
            summary_list.append(summary)

        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
            # Optionally, add placeholder values on error
            title_list.append("N/A")
            summary_list.append("N/A")
    
    return title_list, summary_list
