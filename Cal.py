import os
import time as waktu

os.system('clear')


print("""\033[32;1m
			╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗
			║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝
			╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═
		          ╔════════════════════════=
		          ║  (1) PEMBAGIAN         ║
		          ║  (2) PERTAMBAHAN       ║
		          ║  (3) PENGURANGAN       ║
		          ║  (4) PERKALIAN         ║
		          ║  (5) SISA BAGI         ║
		          ║  (6) PANGKAT           ║
		          ║  (7) PEMBAGIAN PANGKAT ║
		          ║  (8) EXIT              ║
		          ════════════════════════ ╝

""")

pilih = input("\033[37;1mPilih Menu => ")

if pilih == "1":
  bagi_pertama = int(input("\nMasukan Angka Perqtama => "))
  bagi_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_bagi   = bagi_pertama / bagi_kedua
  print(f"\nHasil Dari : {bagi_pertama} / {bagi_kedua} = {hasil_bagi}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "2":
  tambah_pertama = int(input("\nMasukan Angka Pertama => "))
  tambah_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_tambah   = tambah_pertama + tambah_kedua
  print(f"\nHasil Dari : {tambah_pertama} + {tambah_kedua} = {hasil_tambah}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "3":
  kurang_pertama = int(input("\nMasukan Angka Pertama => "))
  kurang_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_kurang   = kurang_pertama - kurang_kedua
  print(f"\nHasil Dari : {kurang_pertama} - {kurang_kedua} = {hasil_kurang}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "4":
  kali_pertama = int(input("\nMasukan Angka Pertama => "))
  kali_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_kali   = kali_pertama * kali_kedua
  print(f"\nHasil Dari : {kali_pertama} * {kali_kedua} = {hasil_kali}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "5":
  sisa_pertama = int(input("\nMasukan Angka Pertama => "))
  sisa_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_sisa   = sisa_pertama % sisa_kedua
  print(f"\nHasil Dari : {sisa_pertama} % {sisa_kedua} = {hasil_sisa}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "6":
  pang_pertama = int(input("\nMasukan Angka Pertama => "))
  pang_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_pang   = pang_pertama ** pang_kedua
  print(f"\nHasil Dari : {pang_pertama} ** {pang_kedua} = {hasil_pang}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "7":
  pempang_pertama = int(input("\nMasukan Angka Pertama => "))
  pempang_kedua   = int(input("\nMasukan Angka Kedua => "))
  hasil_pempang   = pempang_pertama // pempang_kedua
  print(f"\nHasil Dari : {pempang_pertama} // {pempang_kedua} = {hasil_pempang}")
  kembali = input("\nKembali Ke Menu Utama? [Y/N] => ")

  if kembali == "Y":
    os.system('python Cal.py')
  else:
    print("END")

elif pilih == "8":
  os.system('exit')

else:
  os.system('clear')
  print("ERROR KEYWORD!, BACK TO PROGRAM...")
  waktu.sleep(5)
  os.system('python Cal.py')
