## Overview
Fragrance Fusion is a project focused on analyzing perfume similarity based on their ingredients and descriptions using natural language processing (NLP) techniques. It utilizes NLP algorithms along with Selenium for web scraping to recommend perfumes with similar scent profiles.

## Features
- **Cosine Similarity:** Perfume similarity is calculated using cosine similarity between their ingredient vectors.
- **Top 3 Similar Perfumes:** The system provides the top 3 perfumes similar to each perfume in the dataset.
- **NLP Processing:** Perfume descriptions are analyzed using NLP techniques to enhance similarity calculations.
- **Web Scraping with Selenium:** Perfume data is scraped from wikiparfum.com and images are scraped from google.com using Selenium for a comprehensive dataset.
- **Web Application:** An interactive web application allows users to search for perfumes and view recommendations.

## Technologies Used
- Python
- pandas
- scikit-learn
- Flask
- Natural Language Toolkit (NLTK)
- Selenium

## File Structure
- `app.py`: Contains Flask routes to serve the web application.
- `perfumes_batch1.csv`: CSV file containing perfume data including name, brand, ingredients, classification, and description.
- `perfume_similarity_results_top3_nlp.csv`: Output CSV file containing the top 3 similar perfumes for each perfume in the dataset.
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static assets such as images and CSS files.

## Usage
1. **Setup Environment:**
    - Install Python and required dependencies using `pip install -r requirements.txt`.
2. **Run the Application:**
    - Execute `python app.py` to start the Flask server.
    - Access the application in your web browser at `http://127.0.0.1:5000/`.
3. **Search and Explore:**
    - Use the search bar to find perfumes based on brand, name, or description.
    - Click on a perfume to view its top 3 similar perfumes.

## About the Data
The dataset contains information about various perfumes including their name, brand, ingredients, classification, and description. Perfume descriptions are processed using NLP techniques to enhance similarity analysis. Data is collected by scraping wikiparfum.com for information and images are scraped from google.com using Selenium.

## Methodology
1. **Data Collection with Selenium:**
    - Utilize Selenium to scrape perfume data from wikiparfum.com and images from google.com.
2. **Data Preprocessing:**
    - Standardize text data, fill missing values, and tokenize ingredients.
3. **Vectorization:**
    - Utilize TF-IDF Vectorizer to convert text data into numerical vectors.
4. **Similarity Calculation:**
    - Calculate cosine similarity between perfume ingredient vectors.
5. **NLP Processing:**
    - Analyze perfume descriptions using NLP techniques such as tokenization and text normalization.
6. **Web Application Development:**
    - Build an interactive web application using Flask and Gradio to visualize and explore perfume recommendations.

## Future Improvements
- Incorporate advanced NLP models such as BERT or GPT for more accurate analysis of perfume descriptions.
- Enhance the user interface of the web application with more interactive features and visualizations.
- Optimize web scraping process for faster data collection and better scalability.
