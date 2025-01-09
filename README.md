Multilingual Search Engine for Analysis of COVID related tweets on Twitter (Solr, AWS):

This project involves building a multilingual search engine to analyze COVID-related tweets from Twitter, using tools and frameworks like Solr, AWS, Django, and Python.
 Here's a detailed breakdown of the project and its components:
1. Objective:
•	Build an information retrieval (IR) system for COVID-related tweets.
•	Enable multilingual support to process tweets in three different languages.
•	Perform sentiment analysis and topic categorization to extract insights.
•	Provide a user-friendly web interface for searching and exploring tweets.

2. Key Components:

a. Content Ingestion:
•	Use Twitter API to extract tweets containing COVID-related keywords.
•	Preprocess the tweets (e.g., remove special characters, normalize text, handle language-specific nuances).
•	Store the preprocessed tweets, supporting multilingual text.

b. Indexing with Solr:
•	Configure Apache Solr as the search engine backend.
•	Design a schema to store tweet metadata (e.g., text, language, timestamp, sentiment score, topics).
•	Index around 300,000 tweets for efficient search and filtering.

c. Sentiment Analysis:
•	Perform sentiment analysis (positive, negative, neutral) using Python libraries like TextBlob.
•	Support multilingual sentiment analysis with language-specific models or tools.

d. Topic Categorization:
•	Use topic modeling techniques like Latent Dirichlet Allocation (LDA) embeddings to categorize tweets into topics (e.g., Vaccines, Lockdown, Variants).
•	Store the topics alongside tweets in the Solr index for filtering.

e. Web Application:
•	Developed a Django-based web application:
o	A search bar for querying indexed tweets.
o	Filters for language, sentiment, and topics.
o	A visualization dashboard to display statistics (e.g., tweet sentiment distribution, trending topics).
•	Use HTML/CSS/JavaScript for front-end design.

f. AWS Integration:
•	Host the Solr instance, web application, and database on AWS services 
