from pridobi_podatke import getIMDBdata
import pandas as pd

# Funkcija za pretvorbo v int
def pretvori_glasove(vrednost):
    vrednost = str(vrednost).strip().replace(',', '').upper()
    try:
        if vrednost.endswith('M'):
            return int(float(vrednost[:-1]) * 1_000_000)
        elif vrednost.endswith('K'):
            return int(float(vrednost[:-1]) * 1_000)
        else:
            return int(vrednost)
    except:
        return 0

def tabela_milijon_plus():
    naslovi, ocene, stevilo_glasov, leto_izdaje, zanr = getIMDBdata()

    df = pd.DataFrame({
        'Naslovi': naslovi,
        'Ocene': ocene,
        'Število glasov': stevilo_glasov,
        'Leto izdaje': leto_izdaje,
        'Žanr': zanr
    })

    # 'Število glasov' v int
    df['Število glasov'] = df['Število glasov'].apply(pretvori_glasove)

    # Samo filmi z več kot 2 M glasov
    df_filtriran = df[df['Število glasov'] > 2_000_000]

    df_filtriran.to_csv('imdb_movies_2Mplus.csv', index=False, encoding='utf-8')
    print("📄 CSV 'imdb_movies_2Mplus.csv' z več kot 1M glasovi je bil ustvarjen.")

tabela_milijon_plus()

