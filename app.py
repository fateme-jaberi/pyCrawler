# a program that will extract the list of the newest questions on stackoverflow.com
# On the first 3 pages.

# examples of endpoints in stackoverflow.com:
# https://stackoverflow.com/questions?tab=newest&page=2
# https://stackoverflow.com/questions?tab=newest&page=3

import requests
from bs4 import BeautifulSoup

pages = range(1, 4)

for page in pages:
    # download the page
    response = requests.get(
        "https://stackoverflow.com/questions?tab=newest&page=" + "page"
    )

    soup = BeautifulSoup(response.text, "html.parser")
    questions = soup.select(".s-post-summary")  # returns a list

    for question in questions:
        print(question.select_one(".s-link").getText())  # returns title
    print(
        question.select_one(".s-post-summary--stats-item-number").getText()
    )  # returns votes
