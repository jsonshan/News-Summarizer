import requests
import google.generativeai as genai
from bs4 import BeautifulSoup

instruction_summary = {
  "You are a news summarization expert who specializes in creating concise and easy-to-understand summaries. " \
  "When I provide a link or describe a news article, please generate a summary that is clear and captures the " \
  "essential details in 1-3 paragraphs. Do not give explanations or analysis beyond the summary itself. "
}

model = genai.GenerativeModel(
  "models/gemini-1.5-flash", system_instruction=instruction_summary
)

instruction_category = {
  "You are a web scraping and article categorization expert specializing in identifying and classifying articles from a list of URLs. " \
  "When I provide a URL, extract all hyperlinks that are likely to be articles based on the presence of the year '2024' in the URL or content. " \
  "Further narrow down by filtering out links that are not news, articles, or stories by checking for relevant keywords ('news', 'article', 'story', etc.). " \
  "Classify any extracted articles into the following categories: 'World', 'Finance', 'Business', 'Technology', 'Pop Culture', 'Entertainment', 'Politics', 'Sports', or 'Other' based on their content. " \
  "Do not provide explanations. Return the category, article title, and source if available, alongside the article URL."
}

model_category = genai.GenerativeModel(
  "models/gemini-1.5-flash", system_instruction=instruction_category
)

def generate_summary(content):
  try:
    response = model.generate_content(content)

    return response.text
  except ValueError as e:
    if "safety_ratings" in str(e):
      print("The content could not be summarized because it contains potentially explicit or harmful material.")
    else:
      print("An error occurred while generating the summary:", e)