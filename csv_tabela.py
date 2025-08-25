from pridobi_podatke import getIMDBdata
import pandas as pd


def tabela():
    naslovi, ocene, stevilo_glasov, leto_izdaje, zanr = getIMDBdata()

    df = pd.DataFrame({
        'Naslovi': naslovi,
        'Ocene': ocene,
        'Število glasov': stevilo_glasov,
        'Leto izdaje': leto_izdaje,
        'Žanr': zanr
    })

    df.to_csv('imdb_movies.csv', index=False, encoding='utf-8')
    print("📄 CSV datoteka 'imdb_movies.csv' je bila uspešno ustvarjena.")

tabela()

