"""
Modularisasi dengan function
"""
from scrape_data_bmkg import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    data_gempa = ekstraksi_data()
    tampilkan_data(data_gempa)
    



    


