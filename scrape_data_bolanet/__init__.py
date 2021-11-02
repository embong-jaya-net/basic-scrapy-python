import requests
from bs4 import BeautifulSoup


def ekstraksi_data_bolanet():
    try:
        content = requests.get('https://www.bola.net/champions/')
    except Exception:
        return None

    if content.status_code == 200:

        soup = BeautifulSoup(content.text, 'html.parser')
        scrap = soup.find('div', {'class': 'item'})
        # scrap = scrap.findChildren('div', {'class': 'text'})
        # scrap = scrap.findChildren('a', {'class': 'ntitle'})
        # scrap = scrap.text
        print(scrap.prettify())








