import requests
from bs4 import BeautifulSoup


def ekstraksi_data_bolanet():
    try:
        content = requests.get('https://www.bola.net/champions/')
    except Exception:
        return None

    if content.status_code == 200:

        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find_all('a', {'class': 'ntitle'})
        time = soup.find_all('span', {'class': 'date'})

        for judul in title:
            print(judul.text)


# ekstraksi_data_bolanet()

