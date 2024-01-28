import requests
from bs4 import BeautifulSoup

# Send a request to the webpage
url = 'https://www.sellyourmac.com/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the prices section of the webpage
prices_section = soup.find('section', {'id': 'prices'})

# Extract the data for each device from the prices section
devices = []
for item in prices_section.find_all('div', {'class': 'item'}):
    device_name = item.find('h4').text.strip()
    device_description = item.find('p', {'class': 'description'}).text.strip()
    device_image = item.find('img')['src']
    options = []
    for option in item.find_all('div', {'class': 'option'}):
        option_name = option.find('div', {'class': 'name'}).text.strip()
        option_description = option.find('div', {'class': 'description'}).text.strip()
        option_price = option.find('div', {'class': 'price'}).text.strip()
        options.append({'name': option_name, 'description': option_description, 'price': option_price})
    devices.append({'name': device_name, 'description': device_description, 'image': device_image, 'options': options})

# Print the data for each device
for device in devices:
    print(device['name'])
    print(device['description'])
    print(device['image'])
    for option in device['options']:
        print(f"- {option['name']}: {option['description']}, {option['price']}")
    print()
