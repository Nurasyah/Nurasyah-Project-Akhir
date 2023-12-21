import os

os.system("cls")

import datetime
from getpass import getpass
import random

hari_ini = datetime.date.today()

# DATA REKENING
print("SELAMAT DATANG DI ATM SEJAHTERA")
nama = input("MASUKAN NAMA :")
chance = 2
pin = getpass("MASUKAN PIN ANDA :")
min_saldo = 1000000
max_saldo = 5000000
random_saldo = random.randint(min_saldo, max_saldo)
saldo = random_saldo
riwayat_transaksi = []

def menu_utama():
    print(f'{"MENU UTAMA":^40}')
    print("-" * 40)
    print("1. INFORMASI SALDO       3. SETOR TUNAI")
    print("2. PENARIKAN TUNAI       4. TRANSFER")
    

def validasi_nominal(tarik_tunai):
    if tarik_tunai < 50000:
        print("MINIMAL PENARIKAN Rp50")
        return False

    if tarik_tunai % 50000 != 0:
        print("Harus kelipatan 50rb atau 100rb")
        return False
    return True
        
def cek_saldo_cukup(tarik_tunai):
    if tarik_tunai > saldo:
        print("Maaf, saldo Anda tidak mencukupi")
        return False
    else:
        return True
    
def transfer():
    print(f'{"TRANSFER ANTAR BANK":^40}')
    print(f"{40*'*'}")


def validasi_transfer(jumlah):
    # Validasi saldo cukup
    if jumlah > saldo:
        print("Maaf, saldo tidak mencukupi")
        return False
    if jumlah % 50000 != 0:
        print("Transfer harus kelipatan 50rb atau 100rb")  
        return False
    return True

def menu_keluar():
    exit()  

while chance >= 0:
    input_pin = getpass(" KONFIRMASI PIN ATM ANDA  : ")
    if input_pin != pin:
        print("PIN YANG ANDA MASUKAN SALAH")
        chance = chance - 1
    if chance == 0:
        print("Kesempatan Untuk Mencoba Telah Habis, Kartu Anda Terblokir")
        print("=" * 40)
        print()
        break
    if input_pin == pin:
        menu_utama()
        pilihan = int(input("PILIH MENU :"))
        if pilihan == 1:
            print(f'{"INFORMASI SALDO":^40}')
            print(f"{40*'*'}")
            print(f"       HALO {nama}, SALDO ANDA SEBESAR")
            print(f"                Rp{saldo:,}           ")
            print(f"{40*'-'}")
            lagi = int(input("\nLANJUT TRANSAKSI LAIN? \n1. YA \n2. TIDAK\n"))
            if lagi == 1:
                continue
            else:
                break
        elif pilihan == 2:
            tarik_tunai = int(input("MASUKAN NOMINAL PENARIKAN :"))
            if not validasi_nominal(tarik_tunai):
                continue
            else:
                saldo -= tarik_tunai
            if not cek_saldo_cukup(tarik_tunai):
                continue
            saldo -= tarik_tunai
            print(f'{"STRUK PENARIKAN":^40}')
            print("-" * 40)
            print(f"Nama                :{nama}")
            print(f"Tarik Tunai         :{tarik_tunai:,}")
            print(f"Tanggal Penarikan   :{hari_ini}")
            print(f"Sisa Saldo          :{saldo :,}")
            lagi = int(input("\nLANJUT TRANSAKSI LAIN? \n1. YA \n2. TIDAK\n"))
            if lagi == 1:
                continue
            else:
                break
        elif pilihan== 3:
            setor_tunai = int(input("MASUKKAN NOMINAL SETOR \n"))
            if setor_tunai % 50000 != 0:
                print("SETORAN HARUS KELIPATAN Rp50 atau Rp100")
                continue
            saldo += setor_tunai
            print(f'{"STRUK SALDO TUNAI":^40}')
            print("-" * 40)
            print(f"Nama \t             :{nama}    ")
            print(f"Nominal Setoran \t  :{setor_tunai:,} ")
            print(f"Tanggal Penarikan \t :{hari_ini} ")
            print(f"Sisa Saldo   \t      :Rp{saldo :,}")
            lagi = int(input("\nLANJUT TRANSAKSI LAIN? \n1. YA \n2. TIDAK\n"))
            if lagi == 1:
                continue
            else:
                break
        elif pilihan== 4:
            jumlah = int(input("MASUKAN NOMINAL TRANSFER: "))
            if not validasi_transfer(jumlah):
                continue
            bank_tujuan = input("Masukkan nama bank tujuan: ")
            bank_asal = input("Masukkan nama bank asal: ")
            norek_tujuan = input("Masukkan no rekening tujuan: ")
            nama_pengirim = input("Masukkan nama pengirim: ")
            nama_penerima = input("Masukkan nama penerima: ")
            print(f"\nProses transfer Rp{jumlah:,} ke {bank_tujuan}")
            konfirmasi = input("Konfirmasi (y/n)? ")
            if konfirmasi == "y":
                saldo -= jumlah
                print("Transfer berhasil")
                # Menambahkan bukti transfer
                print(f"\n{'BUKTI TRANSFER':^40}")
                print(f"{40*'*'}")
                print(f"Ke Bank         : {bank_tujuan} ")
                print(f"Dari Bank       : {bank_asal}   ")
                print(f"Nama Pengirim   : {nama_pengirim}")
                print(f"Nama Penerima   : {nama_penerima}")
                print(f"No. Rekening    : {norek_tujuan} ")
                print(f"Jumlah          : Rp{jumlah:,}  ")
                print(f"Tanggal         : {hari_ini}     ")
                print(f"       TRANSAKSI BERHASIL       ")
                print(f"{40*'-'}")
                lagi = int(input("\nLANJUT TRANSAKSI LAIN? \n1. YA \n2. TIDAK\n"))
            if lagi == 1:
                continue
            else:
                print("Transfer dibatalkan")
            break
    
print("TERIMAHKASIH ATAS KUNJUNGANYA")
print("AMBIL KARTU ANDA")
             