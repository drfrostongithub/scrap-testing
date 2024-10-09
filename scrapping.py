import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://www.youtube.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.status_code)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags (<a>)
    links = soup.find_all('a')
    
    # Extract the href attribute from each <a> tag
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
