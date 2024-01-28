
import requests
import re
from bs4 import BeautifulSoup 
# Send a GET request to the map URL
response = requests.get('https://example.com/map')

# Parse the HTML code with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
    # Find the location names and addresses in the HTML code
locations = soup.findAll('div', {'class': 'location'})
# Extract the location name and address from each HTML element
for location in locations:
    name = location.find('h2').text
    address = location.find('p', {'class': 'address'}).text

    print(name, address)
