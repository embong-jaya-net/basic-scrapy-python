import requests
from bs4 import BeautifulSoup


def ekstraksi_data_bmkg():

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        scrap = soup.find('span', {'class': 'waktu'})
        scrap = scrap.text.split(',')
        tanggal = scrap[0]
        waktu = scrap[1]

        scrap = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        scrap = scrap.findChildren('li')
        magnitudo = None
        kedalaman = None
        i = 0
        for data in scrap:
            # print(i, data)
            if i == 1:
                magnitudo = data.text
            elif i == 2:
                kedalaman = data.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman

        return hasil


def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
