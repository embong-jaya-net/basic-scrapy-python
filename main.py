"""
Modularisasi dengan function
"""


def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = 4.1
    hasil['kedalaman'] = '70 KM'

    return hasil


def tampilkan_data(result):
    print("Gempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    data_gempa = ekstraksi_data()
    tampilkan_data(data_gempa)
    



    


