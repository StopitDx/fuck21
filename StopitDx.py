#!/bin/system login/kasir restoran/python

import os,sys,time

x = "r"
y = "r"

def login():
    print("=" * 58)
    print("                 HALAMAN LOGIN KASIR")
    print("=" * 58)
    user = input("¤> Masukan username : ")
    passw = input("¤> Masukan  Password : ")
    if user ==x and passw ==y:
       print ("Akses Diterima..")
       #print ("Login Berhasil..\n\n")
       time.sleep(2)
       
#def main_menu():
   # membuat daftar menu pada kasir
    print('=' * 16, 'MAIN MENU APLIKASI KASIR', '=' * 16)
    print('          selamat datang di menu aplikasi kasir')
    print('=' * 17, 'masukan input aplikasi', '=' * 17)
    print('1. Program kasir')
    print('2. program kalkulator')
    print('3. exit program')
    
#   input pilihan #
    pilihan = input('pilih menu : ')
#   pilihan menu #
    if pilihan == '1':
    
      
#Membuat Program Aplikasi Inputan User Kasir)#
       nama_barang = input("Masukan nama barang : ")
       harga = int(input('masukan harga barang : '))
       jumlah_beli = int(input('masukan jumlah barang : '))
# mengitung jumlah harga
       total = harga * jumlah_beli
# cetak total harga
       print(f'harga total : {nama_barang}, = {total}')
# input pembayaran dari user
       bayar = int(input('masukan pembayaran : '))
# mengecek apakah pembayaran kurang atau ada kembalian
       kurang = total - bayar
       kembalian = bayar - total
       
    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
#        tanya()
        
    elif bayar == total:
        print('uang anda pas,terimakasih telah berbelanja ')
    else:
        print(f'maaf uang anda tidak cukup,uang anda kurang {kurang}')
#        counter_kasir()

#Membuat Program Aplkasi kalkulator


#def tanya():
    tanya = input('kembali ke menu..? (y/n)')
    if tanya == 'y':
  #      main_menu()
    #elif tanya == 't':
         exit()
      
    else:
       print ("Akses Ditolak..")
       time.sleep(2)
      
       
       os.system("python Login.py")
if __name__ == "__main__":
     login()