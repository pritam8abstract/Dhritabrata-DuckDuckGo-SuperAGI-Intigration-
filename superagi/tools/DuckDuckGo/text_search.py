# text_search.py
from duckduckgo_search import DDGS

# create an instance of the DDGS class
ddgs = DDGS()

# get the keywords from the user input
keywords = input("Enter your query: ")

# perform the text search and get the results as a generator
results = ddgs.text(keywords, region="wt-wt", safesearch="Moderate", timelimit="y")

# iterate over the results and print them
for result in results:
    print(result)