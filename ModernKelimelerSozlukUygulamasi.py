# Modern kelimeleri ve anlamlarını saklamak için bir sözlük (dictionary)
meme_dict = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

# Selamlama mesajı ve talimatlar
print("Hoş geldiniz! Bu uygulama modern kelimelerin anlamlarını bulmanıza yardımcı olacak.")
print("Lütfen anlamadığınız bir kelimeyi yazın (hepsini büyük harflerle yazın!). Çıkmak için 'ÇIK' yazın.\n")

# Kullanıcıdan giriş almak ve işlemleri döngüde gerçekleştirmek
for _ in range(5):  # Programı tek seferde 5 kelime soracak şekilde döngüye sokuyoruz
    word = input("Anlamadığınız bir kelime yazın: ").strip().upper()
    
    if word == 'ÇIK':
        print("Uygulamadan çıkılıyor...")
        break
    
    if word in meme_dict:
        print(f"{word} - {meme_dict[word]}")
    else:
        print(f"Üzgünüm, '{word}' kelimesinin anlamını bilmiyorum. Lütfen başka bir kelime deneyin.\n")

print("Teşekkürler! Uygulamamızı kullandığınız için teşekkür ederiz.")
