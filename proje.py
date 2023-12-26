from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from user import username,password

options = webdriver.EdgeOptions()
browser = webdriver.Edge(options=options)

# Hangi kullanıcının Takipçi/Takip listesini almak istiyorsanız giriniz.
kullanici_id_gir = input("\nKullanıcı ID gir\n")

while not kullanici_id_gir:
    kullanici_id_gir = input("\nKullanıcı ID gir: ")

def start():
    insta = "https://www.instagram.com/"
    browser.maximize_window()
    browser.get(insta)
    time.sleep(2)

# Kullanıcı Girişi
def kullanici_giris():
    user_name = browser.find_element(By.NAME,"username")
    user_password = browser.find_element(By.NAME,"password")
    user_name.send_keys(username)
    user_password.send_keys(password)
    giris_button = browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button")
    giris_button.click()
    time.sleep(5)

def takipciler_butonu():
    browser.get(f"https://www.instagram.com/{kullanici_id_gir}/followers/")
    time.sleep(5)
def takip_butonu():
        browser.get(f"https://www.instagram.com/{kullanici_id_gir}/following/")
        time.sleep(5)

def kaydirma():
    # JavaScript komutu
    js_command = """
        var sayfa = document.querySelector('._aano');
        sayfa.scrollTo(0, sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
    sayfa_sonu = int(browser.execute_script(js_command))

    while True:
        son = sayfa_sonu
        time.sleep(1.2)
        sayfa_sonu = int(browser.execute_script(js_command))

        if son == sayfa_sonu:
            break    
# Takipci dosya yazma
def takip_dosya_yazma():
    sayac = 0
    takipcilist = []
    takipciler = browser.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")
    for takipci in takipciler:
        sayac += 1
        print(str(sayac) + " --> " + takipci.text)
        takipcilist.append(takipci.text)

    with open("takipçiler.txt", "w", encoding="UTF-8") as file:
        for takipciler in takipcilist:
            file.write(takipciler + "\n")

# Takip edilen dosya yazma
def takip_edilen_yazma():
    sayac = 0
    takipcilist = []
    takipciler = browser.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")
    for takipci in takipciler:
        sayac += 1
        print(str(sayac) + " --> " + takipci.text)
        takipcilist.append(takipci.text)

    with open("takip_edilenler.txt", "w", encoding="UTF-8") as file:
        for takipciler in takipcilist:
            file.write(takipciler + "\n")            

def reklam_kaldirma():
    try:
        reklam_kaldir = browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        time.sleep(10)
        reklam_kaldir.click()
    except Exception as hata:
        print(f"Reklam yok : {hata}")
try:
    reklam_kaldirma()

except Exception as hata:
    print(f"Hata : {hata}")
else:
    print("Program Çalışıyor....")
finally:
    start()

    kullanici_giris()

    reklam_kaldirma()

    print("****Takip Edenler***")
    takipciler_butonu()
    kaydirma()
    takip_dosya_yazma()
    print("\nTakip Edenler dosyaya yazıldı\n")

    print("****Takip Ettikleri***")
    takip_butonu()
    kaydirma()
    takip_edilen_yazma()
    print("\nTakip Ettikleri dosyaya yazıldı\n")

    browser.quit()

