from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def getIMDBdata():
    # Path to your chromedriver.exe
    POT_DO_CHROME_GONILNIKA = r'C:\chromedriver.exe'

    # Dodatno: pot do Google Chrome (ker ni v standardni lokaciji)
    chrome_nastavitve = Options()
    chrome_nastavitve.binary_location = r'C:\Users\Zala\AppData\Local\Google\Chrome\Application\chrome.exe'

    # Set up WebDriver
    service = Service(POT_DO_CHROME_GONILNIKA)
    driver = webdriver.Chrome(service=service, options=chrome_nastavitve)
    
    try:
        # Open IMDb Top 250 movies page
        driver.get('https://www.imdb.com/chart/top/')

        # Wait for page to load (simple sleep for demo, better to use explicit waits)
        time.sleep(10)

        driver.find_element(By.CSS_SELECTOR, '.ddtuHe').click()

        # Find all movie rows
        filmi = driver.find_elements(By.CSS_SELECTOR, '.ipc-metadata-list-summary-item')
        
        naslovi = []
        ocene = []
        st_glasov = []
        leta = []
        zaner = []
        premakni_y_za_px = 118
        for film in filmi:
            if (premakni_y_za_px != 118):
                scroll = int(film.rect['y']) - premakni_y_za_px
                ActionChains(driver).scroll_by_amount(0,scroll).perform()
            else:
                ActionChains(driver).scroll_by_amount(0,premakni_y_za_px).perform()
            premakni_y_za_px = int(film.rect['y'])
            naslov = film.find_element(By.CSS_SELECTOR, 'div.ipc-title').text
            # Remove the number at the start of the string
            naslovi.append(naslov[naslov.find(" ")+1:])
            ocene.append(film.find_element(By.CSS_SELECTOR, '.ipc-rating-star--rating').text)
            st_glasov.append(film.find_element(By.CSS_SELECTOR, '.ipc-rating-star--voteCount').text.replace("(", "").replace(")",""))
            leta.append(film.find_element(By.CSS_SELECTOR, 'span.sc-15ac7568-7').text)
            film.find_element(By.CSS_SELECTOR, 'button.ipc-icon-button--base').click()
            time.sleep(0.5)
            popup = driver.find_element(By.CSS_SELECTOR, 'div.eyorye').find_elements(By.CSS_SELECTOR, 'ul.ipc-inline-list')[1];
            zanri = popup.find_elements(By.CSS_SELECTOR, 'li.ipc-inline-list__item')
            rezultat = ""
            for zanr in zanri:
                rezultat += zanr.text + ' '
            zaner.append(rezultat)
            driver.find_element(By.CSS_SELECTOR, 'button.ipc-icon-button--baseAlt').click()
            time.sleep(0.3)
        
        ocene = pretvori_v_dec_stevilo(ocene)
        leta = pretvori_v_int_stevilo(leta)

        return naslovi, ocene, st_glasov, leta, zaner

    finally:
        driver.quit()

def pretvori_v_dec_stevilo(stevila):
    for indeks,niz in enumerate(stevila):
        stevila[indeks] = float(niz)
    return stevila

def pretvori_v_int_stevilo(stevila):
    for indeks,niz_stevilo in enumerate(stevila):
        stevila[indeks] = int(niz_stevilo)
    return stevila