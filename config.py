from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime
import random
import urllib.parse

class LinkedInBot:
    def __init__(self):
        print(f"[{self.get_time()}] Bot başlatılıyor...")
        self.setup_driver()
        
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")
    
    def setup_driver(self):
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-notifications')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--lang=tr-TR')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self, username, password):
        try:
            print(f"[{self.get_time()}] LinkedIn'e giriş yapılıyor...")
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            
            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            
            username_field.send_keys(username)
            password_field.send_keys(password)
            
            login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            login_button.click()
            
            time.sleep(5)
            print(f"[{self.get_time()}] Giriş başarılı!")
            return True
            
        except Exception as e:
            print(f"[{self.get_time()}] Giriş hatası: {str(e)}")
            return False
            
    def send_connection_requests(self, keywords=['python developer'], max_requests=25):
        daily_requests = 0
        
        for keyword in keywords:
            if daily_requests >= max_requests:
                print(f"[{self.get_time()}] Günlük limit doldu ({max_requests} istek)")
                break
                
            print(f"[{self.get_time()}] '{keyword}' için arama yapılıyor...")
            
            encoded_keyword = urllib.parse.quote(keyword)
            search_url = f"https://www.linkedin.com/search/results/people/?keywords={encoded_keyword}&origin=GLOBAL_SEARCH_HEADER"
            
            self.driver.get(search_url)
            time.sleep(5)
            
            page = 1
            while daily_requests < max_requests:
                try:
                    self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-container")))
                    
                    # Sayfayı aşağı kaydır
                    for _ in range(3):
                        self.driver.execute_script("window.scrollBy(0, 500)")
                        time.sleep(1)
                    
                    # Farklı bağlantı butonu seçicilerini dene
                    connect_buttons = []
                    selectors = [
                        "button.artdeco-button--lite",
                        "button.artdeco-button--2",
                        "button.ember-view.artdeco-button",
                        ".artdeco-button--lite",
                        ".pvs-profile-actions__action"
                    ]
                    
                    for selector in selectors:
                        buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        for button in buttons:
                            button_text = button.text.strip().lower()
                            if any(text in button_text for text in ["bağlan", "connect", "follow", "takip"]):
                                connect_buttons.append(button)
                    
                    if not connect_buttons:
                        print(f"[{self.get_time()}] Sayfa {page}: Bağlantı butonu bulunamadı, yeni arama yapılıyor...")
                        break
                    
                    for button in connect_buttons:
                        if daily_requests >= max_requests:
                            break
                            
                        try:
                            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                            time.sleep(2)
                            
                            if button.is_displayed() and button.is_enabled():
                                button.click()
                                time.sleep(2)
                                
                                try:
                                    send_button = self.wait.until(EC.element_to_be_clickable(
                                        (By.CSS_SELECTOR, "button.artdeco-button--primary")))
                                    send_button.click()
                                    
                                    daily_requests += 1
                                    print(f"[{self.get_time()}] Bağlantı isteği gönderildi ({daily_requests}/{max_requests})")
                                    
                                    sleep_time = random.uniform(3, 7)
                                    print(f"[{self.get_time()}] {sleep_time:.0f} saniye bekleniyor...")
                                    time.sleep(sleep_time)
                                except:
                                    print(f"[{self.get_time()}] Gönder butonu bulunamadı, devam ediliyor...")
                                    continue
                        
                        except Exception as e:
                            print(f"[{self.get_time()}] Buton tıklama hatası: {str(e)}")
                            continue
                    
                    page += 1
                    next_url = f"{search_url}&page={page}"
                    self.driver.get(next_url)
                    time.sleep(3)
                    
                except Exception as e:
                    print(f"[{self.get_time()}] Sayfa işleme hatası: {str(e)}")
                    break
                    
    def close(self):
        self.driver.quit()

def main():
    # Aranacak anahtar kelimeler
    KEYWORDS = [
        'software developer',
        'backend developer',
        'frontend developer',
        'full stack developer',
        'yazılım mühendisi',
        'yazılım geliştirici',
        'python developer',
        'java developer',
        'web developer'
    ]
    
    # Kullanıcı bilgileri
    EMAIL = "programcieren@hotmail.com"
    PASSWORD = "591163Eren?"
    
    try:
        bot = LinkedInBot()
        
        if bot.login(EMAIL, PASSWORD):
            while True:
                bot.send_connection_requests(
                    keywords=KEYWORDS,
                    max_requests=25
                )
                
                print(f"[{bot.get_time()}] 24 saat bekleniyor...")
                time.sleep(24 * 60 * 60)
                
    except KeyboardInterrupt:
        print("\nBot durduruldu.")
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
    finally:
        bot.close()

if __name__ == "__main__":
    main() 