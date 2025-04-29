import tkinter as tk
import random

def yazdir():
    girilen_karakter = giris_alani.get()

    yazdiriliyor_pencere = tk.Toplevel(pencere)
    yazdiriliyor_pencere.title("Kuantum Yaş Hesaplayıcı 🤯")
    yazdiriliyor_pencere.geometry("300x120")
    yazdiriliyor_pencere.configure(bg="black")

    animasyon_metni = tk.StringVar()
    animasyon_metni.set("⚙️ Süper bilgisayar çalışıyor")

    label = tk.Label(yazdiriliyor_pencere, textvariable=animasyon_metni, font=("Arial", 11), bg="black", fg="lime")
    label.pack(pady=20)

    def animasyonu_guncelle(i=0):
        dots = "." * (i % 4)
        ses = random.choice(["💥 BİP!", "🔊 DIIING!", "📡 ZZZZT!", "🎶 TIK TIK!"])
        animasyon_metni.set(f"⚙️ Süper bilgisayar çalışıyor{dots}\n{ses}")
        if i < 10:
            pencere.after(150, lambda: animasyonu_guncelle(i+1))
        else:
            yazdiriliyor_pencere.destroy()
            karakteri_goster()

    def karakteri_goster():
        rastgele_yas = random.randint(1, 1000)
        sonuc_pencere = tk.Toplevel(pencere)
        sonuc_pencere.title("Bilimsel Yaş Sonucu 🧪")
        sonuc_pencere.geometry("350x200")
        sonuc_pencere.configure(bg="white")

        yorumlar = [
            "Bebek misin, dinozor musun belli değil!",
            "Senin yaşını çözemedik, uzaylı olabilirsin 👽",
            "Bu yaşla krallık kurulur 👑",
            "Yaş değil, efsane yazıyor burada!",
            "Muhtemelen zaman yolcususun ⏳"
        ]
        yorum = random.choice(yorumlar)

        frame = tk.Frame(sonuc_pencere, bg="yellow", bd=3, relief="groove")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        sonuc_label = tk.Label(frame, text=f"🎉 Tahmin Edilen Yaşınız: {rastgele_yas}", font=("Arial", 14, "bold"), bg="yellow", fg="darkblue")
        sonuc_label.pack(pady=10)

        yorum_label = tk.Label(frame, text=yorum, font=("Arial", 12), bg="yellow", fg="black")
        yorum_label.pack(pady=5)

    animasyonu_guncelle()

pencere = tk.Tk()
pencere.title("Kuantum Yaş Tahmin Robotu 3000")
pencere.geometry("350x250")
pencere.configure(bg="lightblue")

etiket = tk.Label(pencere, text="Yaşınızı tahmin etmemize izin verin 😎", font=("Arial", 12, "bold"), bg="lightblue")
etiket.pack(pady=10)

giris_alani = tk.Entry(pencere, font=("Arial", 14))
giris_alani.pack(pady=5)

yazdir_butonu = tk.Button(pencere, text="YAŞI HESAPLA!", font=("Arial", 11, "bold"), command=yazdir, fg="white", bg="purple")
yazdir_butonu.pack(pady=20)

pencere.mainloop()
import tkinter as tk
import random

def yazdir():
    girilen_karakter = giris_alani.get()

    yazdiriliyor_pencere = tk.Toplevel(pencere)
    yazdiriliyor_pencere.title("Kuantum Yaş Hesaplayıcı 🤯")
    yazdiriliyor_pencere.geometry("300x120")
    yazdiriliyor_pencere.configure(bg="black")

    animasyon_metni = tk.StringVar()
    animasyon_metni.set("⚙️ Süper bilgisayar çalışıyor")

    label = tk.Label(yazdiriliyor_pencere, textvariable=animasyon_metni, font=("Arial", 11), bg="black", fg="lime")
    label.pack(pady=20)

    def animasyonu_guncelle(i=0):
        dots = "." * (i % 4)
        ses = random.choice(["💥 BİP!", "🔊 DIIING!", "📡 ZZZZT!", "🎶 TIK TIK!"])
        animasyon_metni.set(f"⚙️ Süper bilgisayar çalışıyor{dots}\n{ses}")
        if i < 10:
            pencere.after(150, lambda: animasyonu_guncelle(i+1))
        else:
            yazdiriliyor_pencere.destroy()
            karakteri_goster()

    def karakteri_goster():
        rastgele_yas = random.randint(1, 1000)
        sonuc_pencere = tk.Toplevel(pencere)
        sonuc_pencere.title("Bilimsel Yaş Sonucu 🧪")
        sonuc_pencere.geometry("350x200")
        sonuc_pencere.configure(bg="white")

        yorumlar = [
            "Bebek misin, dinozor musun belli değil!",
            "Senin yaşını çözemedik, uzaylı olabilirsin 👽",
            "Bu yaşla krallık kurulur 👑",
            "Yaş değil, efsane yazıyor burada!",
            "Muhtemelen zaman yolcususun ⏳"
        ]
        yorum = random.choice(yorumlar)

        frame = tk.Frame(sonuc_pencere, bg="yellow", bd=3, relief="groove")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        sonuc_label = tk.Label(frame, text=f"🎉 Tahmin Edilen Yaşınız: {rastgele_yas}", font=("Arial", 14, "bold"), bg="yellow", fg="darkblue")
        sonuc_label.pack(pady=10)

        yorum_label = tk.Label(frame, text=yorum, font=("Arial", 12), bg="yellow", fg="black")
        yorum_label.pack(pady=5)

    animasyonu_guncelle()

pencere = tk.Tk()
pencere.title("Kuantum Yaş Tahmin Robotu 3000")
pencere.geometry("350x250")
pencere.configure(bg="lightblue")

etiket = tk.Label(pencere, text="Yaşınızı tahmin etmemize izin verin 😎", font=("Arial", 12, "bold"), bg="lightblue")
etiket.pack(pady=10)

giris_alani = tk.Entry(pencere, font=("Arial", 14))
giris_alani.pack(pady=5)

yazdir_butonu = tk.Button(pencere, text="YAŞI HESAPLA!", font=("Arial", 11, "bold"), command=yazdir, fg="white", bg="purple")
yazdir_butonu.pack(pady=20)

pencere.mainloop()
