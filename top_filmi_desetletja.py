from pridobi_podatke import getIMDBdata
import matplotlib.pyplot as plt

def najbolje_ocenjeni():
    naslovi, ocene, stevilo_glasov, leto_izdaje, zanr = getIMDBdata()

    najboljsi = {}

    leto_trenutno = 1920
    while leto_trenutno < 2030:
        najboljsa_ocena = 0
        ime_najbolje_ocenjenega = ""
        for indeks, leto in enumerate(leto_izdaje):  
            if (leto < (leto_trenutno+10) and leto >= leto_trenutno):
                if (ocene[indeks] > najboljsa_ocena):
                    najboljsa_ocena = ocene[indeks]
                    ime_najbolje_ocenjenega = naslovi[indeks]

        najboljsi[ime_najbolje_ocenjenega] = najboljsa_ocena

        leto_trenutno += 10


    # Timeline graf
    naslovi_filmov = list(najboljsi.keys())
    ocene_filmov = list(najboljsi.values())
    desetletja = list(range(1920, 1920 + len(naslovi_filmov)*10, 10))

    plt.figure(figsize=(16, 4))
    plt.hlines(1, min(desetletja)-5, max(desetletja)+5, color='gray', linewidth=1)
    plt.plot(desetletja, [1]*len(desetletja), 'o', color='skyblue', markersize=10)

    for i in range(len(desetletja)):
        naslov = naslovi_filmov[i]
        if len(naslov) > 15:
            split_pos = naslov.find(' ', len(naslov)//2)
            if split_pos == -1:
                split_pos = len(naslov)//2
            naslov = naslov[:split_pos] + '\n' + naslov[split_pos+1:]

        # Naslovi
        plt.text(desetletja[i], 1.02, f"{naslov}\n({ocene_filmov[i]})", 
                 ha='center', va='bottom', fontsize=8, rotation=30)
        
    # Letnice
    plt.xticks(desetletja, rotation=45, fontsize=9)
    plt.yticks([])

    plt.xlim(min(desetletja)-5, max(desetletja)+5)
    plt.title("Najbolje ocenjeni filmi po desetletjih (IMDB)", fontsize=16)
    plt.gca().spines[['left', 'top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()


najbolje_ocenjeni()



