import requests
import google.generativeai as genai
from bs4 import BeautifulSoup
from model import generate_summary
from grab_news import *

# Define instructions for article categorization and summary generation
instruction_category = {
    "You are an article categorization expert. When I provide a URL, extract the article's title. " \
    "Filter for relevant articles based on keywords like 'news', 'article', or 'story'. " \
    "Only return the article title, without any explanations."
}


model_category = genai.GenerativeModel("models/gemini-1.5-flash", system_instruction=instruction_category)

def extract_valid_articles(article_urls):

    # Initialize lists to store the results
    title_list = []
    summary_list = []

    for url in article_urls:
        try:
            # Extract the title using the generative model
            result = model_category.generate_content([url])

            # Extract title from the model response
            title = result.text.replace("Title: ", "").strip() if result.text else "N/A"
            title_list.append(title)

            # Fetch the article content using url_to_text function
            article_text = url_to_text(url)

            # Generate summary using the article text
            summary = generate_summary(article_text)
            summary_list.append(summary)

        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
            title_list.append("N/A")
            summary_list.append("N/A")

    return title_list, summary_list