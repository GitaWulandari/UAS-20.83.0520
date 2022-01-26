import speech_recognition as sr
engine = sr.Recognizer()
mic = sr.Microphone()
hasil= ""

with mic as source:
    print("Mulai bicara........")
    rekaman = engine.listen(source)
    print("\nWaktu habis!")

    try:
        hasil = engine.recognize_google(rekaman, language = "id.ID")
        print(hasil)
    except:
        print("\nSUARA TIDAK TERDETEKSI!!!")


text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()
