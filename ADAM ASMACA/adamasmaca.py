import random

while True:
    print("""
                ADAM ASMACA


            1 -> OYNA
            2 -> KURALLAR
            3 -> ÇIKIŞ


    """)
    secim = int(input("Seçim yapınız: "))
    if (secim == 3):
        exit()

    elif (secim == 2):
        print("""
        Kurallar: 
        - 3 sefer yanlış harf girme hakkınız var.
        - Kelimeyi 1 kez tahmin etme hakkınız var. Yanlış tahmin sonucunda oyun kaybedilir.
        """)

    elif (secim == 1):
        kategori = {1: ["HAYVAN", "aslan", "papağan", "köstebek", "su aygırı", "timsah"],
                    2: ["MEYVE", "ananas", "avokado", "mango", "hindistan cevizi", "armut"],
                    3: ["FİLM", "harry pottter", "game of thrones", "esaretin bedeli", "zindan adası"],
                    4: ["BİTKİ", "ökse otu", "ısırgan otu", "tere", "ıspanak", "orkide", "papatya"]}
        random1 = random.randint(1, 4)
        random2 = random.randint(1, len(kategori[random1]) - 1)
        kelime = kategori[random1][random2]
        k_uzunlugu = len(kelime)
        desen = list()
        hak = 2

        for i in range(0, k_uzunlugu):
            if (kelime[i] == " "):
                desen.append(" / ")
            else:
                desen.append(" _ ")

        print("KATEGORİ:", kategori[random1][0], "\n")
        for i in desen:
            print(i, end="")
        while True:
            if (hak < 0):
                break
            sayac = 0
            for i in desen:
                if (i == " _ "):
                    sayac += 1
            if (sayac == 0):
                print("\nTEBRİKLER,KAZANDINIZ!")
                break
            harf = input("\n\nLütfen bir harf veya tahmin giriniz: ")
            if (harf == kelime):
                print("\nTAHMİNİNİZ DOĞRU! KELİME: ", kelime)
                break
            else:
                if (len(harf) > 1 and harf != kelime):
                    print("\nYANLIŞ TAHMİN. OYUNU KAYBETTİNİZ")
                    break
                elif (len(harf) == 1):
                    for i in range(0, len(desen)):
                        if (kelime[i] == harf):
                            desen[i] = harf
                        else:

                            if (hak == 2):
                                print("Yanlış harf!")
                                print("""
                                        __________
                                        |         |
                                        |         O
                                        |        
                                        |         
                                        |    
                                        |
                                        |_________
                                        """)
                                hak -= 1
                                break
                            elif (hak == 1):
                                print("Yanlış harf!")
                                print("""
                                        __________
                                        |         |
                                        |         O
                                        |        (|)
                                        |         |
                                        |    
                                        |
                                        |_________
                                        """)
                                hak -= 1
                                break
                            elif (hak == 0):
                                print("Yanlış harf!")
                                print("""
                                        __________
                                        |         |
                                        |         O
                                        |        (|)
                                        |         |
                                        |        ( )
                                        |
                                        |_________
                                        """)
                                print("OYUN BİTTİ")
                                hak -= 1
                                break
                            else:
                                pass

                        print("")
                        for i in desen:
                            print(i, end="")
                else:
                    pass



