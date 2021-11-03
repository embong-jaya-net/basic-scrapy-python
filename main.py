"""
Modularisasi dengan function
"""
from scrape_data_bmkg import ekstraksi_data_bmkg, tampilkan_data
from scrape_data_bolanet import ekstraksi_data_bolanet

if __name__ == '__main__':
    print('\nAplikasi Utama - Scraping Data from Website')
    print('-' * 50)
    print('Pilih Menu :')
    print('1. Srcapping Data Gempa Terkini dari website BMKG')
    print('2. Scrapping Data Berita Liga Champions Terbaru dari Website Bolanet')
    print('3. Coming Soon')
    menu = input('Pilih salah satu menu:')
    if menu == '1':
        print('\n')
        data_gempa = ekstraksi_data_bmkg()
        tampilkan_data(data_gempa)
    elif menu == '2':
        print('\n2. Scraping Berita Liga Champions Terbaru dari Website Bolanet')
        ekstraksi_data_bolanet()
    elif menu == '3':
        print('\nComing Soon')
    else:
        print('\nTidak ada di dalam menu')




    


