from pridobi_podatke import getIMDBdata
import matplotlib.pyplot as plt

def zdruzi_ocene_po_letih():
    naslovi, ocene, stevilo_glasov, leto_izdaje, zanr = getIMDBdata()

    sestevek_ocen = []
    stevilo_vseh_let = []
    povprecna_ocena = []
    oznake_desetletij = []

    leto_trenutno = 1920
    while leto_trenutno < 2030:
        sestevek = 0
        stevilo_filmov = 0
        for indeks, leto in enumerate(leto_izdaje):  
            if (leto < (leto_trenutno+10) and leto >= leto_trenutno):
                sestevek += ocene[indeks]
                stevilo_filmov += 1
        
        sestevek_ocen.append(sestevek)
        stevilo_vseh_let.append(stevilo_filmov)
        oznake_desetletij.append(f"{leto_trenutno}-{leto_trenutno + 9}")
        if stevilo_filmov > 0:
            povprecna_ocena.append(sestevek/stevilo_filmov)
        else:
            povprecna_ocena.append(0)

        leto_trenutno += 10

    # Graf
    plt.figure(figsize=(10, 6))
    plt.ylim(7.75, 8.75)
    plt.bar(oznake_desetletij, povprecna_ocena, color='skyblue')
    plt.xlabel("Desetletje")
    plt.ylabel("Povprečna ocena")
    plt.title("Povprečne IMDb ocene filmov po desetletjih")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    


zdruzi_ocene_po_letih()

