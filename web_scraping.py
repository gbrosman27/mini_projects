import requests
from bs4 import BeautifulSoup
from csv import writer

# Get the website html to be scraped.
response = requests.get("https://www.rithmschool.com/blog")

# Send the above response to beautiful soup and save in variable.
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")  # Find all the articles within the html.

# Create a new csv file that is writeable. Write the titles to a row.
with open("rithm_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    # Loop through the articles and just output the desired element data without tags.
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = article.find("time")["datetime"]

        # Write the data saved in the variables above to the csv document.
        csv_writer.writerow([title, url, date])

