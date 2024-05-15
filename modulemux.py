import os, time




os.system("clear")
print("Welcome To ModuleMux")
print()
print("Note: Tools ini bertujuan untuk menginstall module default yang bisa saja berguna untuk beraktivitas di termux, cocok bagi yang termuxnya kereset/baru download termux")
print()
print("1.install module otomatis")
print("2.list module")
print("3.keluar")
print()

while True:

	select = input("pilih angka: ")

	if select == "1":

		while True:

			Yn = input("anda yakin ingin install module? [Y/n]: ")
			if Yn == "n":
				print("Ok")
				break

			elif Yn == "Y":
				os.system("clear")
				print("Note: jika ingin membatalkan klik ctrl + z")
				print("1.versi pendek (direkomendasi)")
				print("2.versi panjang (kemungkinan membuat ruang penyimpanan full)")
				print()
				sP = input("Pilih Opsi: ")
				if sP == "1":
					os.system("pkg install python2")
					os.system("pkg install ruby")
					os.system("pkg install curl")
					os.system("pkg install wget")
					os.system("pkg install figlet")
					os.system("pkg install php")
					os.system("pkg install nodejs")
					os.system("pkg install toilet")
					os.system("pkg install git")
					os.system("pkg install jq")
					os.system("pip install colorama")
					os.system("pip install requests")
					os.system("pip install mechanize")
					os.system("pip install lolcat")
					os.system("pip install flask")
					os.system("pip install rich")
					os.system("pip install bash")
					os.system("pip install bs4")
					os.system("pkg install python3")
					os.system("clear")
					print("penginstalan selesai, selamat beraktivitas")
					time.sleep(1)
					print("Terima Kasih telah menggunakan tools ini")
					time.sleep(2)
					print("System End 💻")
					sys.exit()

				if sP == "2":
					os.system("pkg install python2")
					os.system("pkg install python3")
					os.system("pkg install curl")
					os.system("pkg install wget")
					os.system("pkg install ruby")
					os.system("pkg install php")
					os.system("pkg install nodejs")
					os.system("pkg install figlet")
					os.system("pkg install toilet")
					os.system("pkg install git")
					os.system("pkg install jq")
					os.system("pip install bash")
					os.system("pip install stdiomask")
					os.system("pip install lolcat")
					os.system("pip install requests")
					os.system("pip install bs4")
					os.system("pip install simplejson")
					os.system("pip install requests")
					os.system("pip install futures")
					os.system("pip install rich")
					os.system("pip install mechanize")
					os.system("pip install cython")
					os.system("pip install licensing")
					os.system("pip install colorama")
					os.system("pip install proxy")
					os.system("pip install telethon")
					os.system("clear")
					print("Penginstalan selesai, selamat beraktivitas kembali")
					time.sleep(1)
					print("Terima Kasih telah menggunakan tools ini")
					time.sleep(2)
					print("System End 💻")
					sys.exit()

			else:
				os.system("clear")
				print("Welcome To ModuleMux")
				print()
				print("Note: Tools ini bertujuan untuk menginstall module default yang bisa saja berguna untuk beraktivitas di termux, cocok bagi yang termuxnya kereset/baru download termux")
				print()
				print("1.install module otomatis")
				print("2.list")
				print("3.keluar")
				print()
				print("pilihan angka: 1")
				print("pilhan tidak ada")

	elif select == "2":
		os.system("clear")
		print("Welcome To ModuleMux")
		print()
		print("Note: Tools ini bertujuan untuk menginstall module default yang bisa saja berguna untuk beraktivitas di termux, cocok bagi yang termuxnya kereset/baru download termux")
		print()
		print("""[Versi Pendek]
pkg update && pkg upgrade
pkg install python
pkg install python2
pkg install ruby
pkg install curl
pkg install wget
pkg install figlet
pkg install php
pkg install nodejs
pkg install toilet
pkg install git
pkg install jq
pip install colorama
pip install requests
pip install mechanize
pip install lolcat
pip install flask
pip install rich
pip install bash
pip install bs4
pkg install python3

[Versi Panjang]
(memungkinkan memakan banyak ruang penyimpanan)
pkg update && pkg upgrade
pkg install python
pkg install python2
pkg install python3
pkg install curl
pkg install wget
pkg install ruby
pkg install php
pkg install nodejs
pkg install figlet
pkg install toilet
pkg install git
pkg install jq
pip install bash
pip install stdiomask
pip install lolcat
pip install requests
pip install bs4
pip install simplejson
pip install requests
pip install futures
pip install rich
pip install mechanize
pip install cython
pip install licensing
pip install colorama
pip install proxy
pip install telethon
""")
		print()
		print("1.install module otomatis")
		print("2.list")
		print("3.keluar")
		print()

	elif select == "3":
		print("Terima Kasih telah mencoba alat ini")
		time.sleep(1)
		print("tetap semangat menjalani aktivitas anda")
		time.sleep(2)
		print("System End 💻")
		break

	else:
		os.system("clear")
		print("Welcome To ModuleMux")
		print()
		print("Note: Tools ini bertujuan untuk menginstall module default yang bisa saja berguna untuk beraktivitas di termux, cocok bagi yang termuxnya kereset/baru download termux")
		print()
		print("1.install module otomatis")
		print("2.list module")
		print("3.exit")
		print("pilihan tidak valid")
		print()

