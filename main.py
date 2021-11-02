"""
Modularisasi dengan function
"""
from scrape_data_bmkg import ekstraksi_data_bmkg, tampilkan_data
from scrape_data_bolanet import ekstraksi_data_bolanet

if __name__ == '__main__':
    print('Aplikasi Utama - Scraping Data from Website')
    print('-' * 50)
    print('\n')
    print('1. Srcapping Data Gempa Terkini dari website BMKG')
    data_gempa = ekstraksi_data_bmkg()
    tampilkan_data(data_gempa)

    print('\n2. Scraping Berita Liga Champions Terbaru dari Website Bolanet')
    ekstraksi_data_bolanet()


    


