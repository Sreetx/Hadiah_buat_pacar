import os, sys, time

print ("#-----------------------------------------------------------------------#")
print ("<|-----------------------Hadiah Untuk Seseorang------------------------|>")
print (" |---------------------------------------------------------------------| ")
print (" | Pembuat:              Lingga Arief Aqiela                           | ")
print (" | Untuk:                Kekasih Incaran                               | ")
print (" | Github:               https://github.com/Sreetx/                    | ")
print (" | Instagram:            https://www.intagram.com/memelucubikin/       | ")
print (" | Kode/Bahasa:          Python                                        | ")
print ("<|---------------------------------------------------------------------|>")
print ("#-----------------------------------------------------------------------#")

while True:
    try:
        print ("[#] Tekan CTRL+C Untuk Keluar")
        print (" [!] Kamu Harus Menjawab Pertanyaan Dari Aku")
        tanya = input("[?] Maukah Kamu Jadi Pacar Aku? [Ya/Tidak]")
        if tanya.lower() == 'ya':
            print ("\n Thank You Sayang...")
            print ("  Aku akan selau bersama mu\n");sys.exit()
        elif tanya.lower() == 'tidak':
            print ("\n Kenapa? Apa ada yang salah")
            print ("  Sudahlah kalau begitu, by\n")
            print (" [#] Keluar\n");sys.exit()
        else:
            print (" [!] Pilihan Yang kamu masukan salah, silakan coba lagi")
            time.sleep(2)
    except KeyboardInterrupt: print (" CTRL+C Terdeteksi, keluar dari program");break
    except EOFError: print (" CTRL+C Terdeteksi, keluar dari program");break
    except Exception as e: print (" ")