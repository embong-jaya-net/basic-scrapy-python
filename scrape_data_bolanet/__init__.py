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

        i = 0
        for i in range(i, len(title)):
            for judul in title[i]:
                print(judul.text)
            for waktu in time[i]:
                print(waktu.text)
        i = i + 1



ekstraksi_data_bolanet()
