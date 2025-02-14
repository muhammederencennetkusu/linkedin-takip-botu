Bu proje, Python ve Selenium kullanarak LinkedIn'de otomatik bağlantı istekleri gönderen bir bot oluşturur. 🔥

📌 Özellikler
✅ LinkedIn'e otomatik giriş yapar.
✅ Belirtilen anahtar kelimelere göre kişi arar.
✅ Bağlantı isteklerini otomatik olarak gönderir.
✅ Günlük belirlenen limit kadar istek gönderir ve 24 saat bekler.
✅ İnsan gibi davranması için rastgele bekleme süreleri eklenmiştir.

🚀 Kurulum
1️⃣ Gerekli Paketleri Yükleyin
Öncelikle, Selenium kütüphanesini yükleyin:

bash
Kopyala
pip install selenium
Ayrıca, Chrome WebDriver indirdiğinizden emin olun. Uygulamanızın Google Chrome sürümüne uygun WebDriver’ı şu adresten indirebilirsiniz:
🔗 https://chromedriver.chromium.org/downloads

2️⃣ WebDriver Yolunu Güncelleyin
Eğer chromedriver.exe dosyanız belirli bir dizindeyse, kod içinde WebDriver’ın yolunu güncelleyin:

python
Kopyala
self.driver = webdriver.Chrome(executable_path="C:/path/to/chromedriver.exe", options=options)
3️⃣ Kullanıcı Bilgilerini Güncelleyin
LinkedIn kullanıcı adı ve şifrenizi main() fonksiyonuna ekleyin:

python
Kopyala
EMAIL = "linkedin_email@example.com"
PASSWORD = "your_password"
⚠️ Güvenlik Uyarısı: Şifrenizi doğrudan kod içine yazmak yerine, bir .env dosyasına koyup dotenv kütüphanesi ile çekmenizi öneririm.

4️⃣ Çalıştırın! 🚀
Botu başlatmak için şu komutu çalıştırın:

bash
Kopyala
python linkedin_bot.py
⚙️ Çalışma Mantığı
LinkedIn’e giriş yapar.
Anahtar kelimeler ile kişileri arar.
Bağlantı istekleri gönderir.
Günlük limite ulaştığında bekler.
📌 Kullanılan Teknolojiler
Python 3.x
Selenium
Google Chrome + WebDriver
🛠 Geliştirme Planları
✅ Şu an: Bağlantı isteği gönderme
🔜 Gelecekte: Kişiye özel mesaj gönderme

⚠️ Yasal Uyarı
Bu bot, LinkedIn'in kullanım koşullarına aykırı olabilir. Hesabınızın askıya alınmaması için, bağlantı isteklerini sınırlı tutun ve botu dikkatli kullanın. Kendi sorumluluğunuzdadır!

📌 Geri bildirimlerinizi bekliyorum! Eğer bir hata ile karşılaşırsanız, pull request veya issue açabilirsiniz.
