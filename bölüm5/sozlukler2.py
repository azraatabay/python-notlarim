sozluk={"kedi":"cat","kalem":"pencil","elma":"apple","pen":"dolma kalem"}
for i in sozluk:
    print("Türkçe:" ,i, "İngilizce:",sozluk[i])
#sözlük içindekileri alt alta yazdırır

print(sozluk.items()) #sözlük içindeki key-value değerlerine aynı anda ulaşmayı sağlar

for i in sozluk[i]:
    print("key:",i,"value:",sozluk[i])
