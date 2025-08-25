from pridobi_podatke import getIMDBdata
import matplotlib.pyplot as plt

def zdruzi_ocene_po_zanrih():
    naslovi, ocene, stevilo_glasov, leto_izdaje, zanri = getIMDBdata()

    zanri_vsi = []
    sestevek_ocen = []
    stevilo_ocen = []
    povprecna_ocena = []

    for indeks, zanr in enumerate(zanri):
        zanr2 = zanr.split(" ")
        for en_zanr in zanr2:
            if en_zanr == '' or en_zanr == ' ': continue
            if en_zanr in zanri_vsi:
                indeks_v_zanri_vsi = zanri_vsi.index(en_zanr)
                sestevek_ocen[indeks_v_zanri_vsi] += ocene[indeks]
                stevilo_ocen[indeks_v_zanri_vsi] += 1
            else:
                zanri_vsi.append(en_zanr)
                sestevek_ocen.append(ocene[indeks])
                stevilo_ocen.append(1)


    for indeks,zanr in enumerate(zanri_vsi):
        povprecna_ocena.append(sestevek_ocen[indeks] / stevilo_ocen[indeks])


    # Graf
    plt.figure(figsize=(10, 6))
    plt.ylim(8.0, 8.75)
    plt.bar(zanri_vsi, povprecna_ocena, color='olive')
    plt.xlabel("Žanr")
    plt.ylabel("Povprečna ocena")
    plt.title("Povprečne IMDb ocene filmov po žanrih")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    


zdruzi_ocene_po_zanrih()