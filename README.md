# Projektna naloga - Analiza filmov
 
 *Avtor: Zala Perpar*

 ## Uvod in ideja

V sledeči projektni nalogi sem predstavila analizo lestvice 250 najbolje ocenjenih filmov, ki sem jo pridobila s spletne strani [IMDb](https://www.imdb.com/chart/top/). Zanimali so me najbolj priljubljeni filmi glede na čas nastanka ter žanra. 

## Navodila

Uporabnik mora naložiti sledeče knjižnice:
- `pandas`,
- `matplotlib`,
- `selenium`,
- `time`.

Odprite datoteko z razširitvijo .ipynb (Jupyter Notebook). Najdeto jo v isti mapi kakor README.md datoteko. Windows uporabniki lahko datoteko zaženete z ukazom 'py -m notebook' v mapi, kjer se nahaja .ipynb datoteka. Nato zaženite vsak korak v .ipynb datoteki posamezno.

## Opis datotek

1. Program `pridobi_podatke.py` iz zgoraj navedene spletne strani pridobi podatke, natančneje; naslov, oceno, število glasov, leto izdaje ter žanr posameznega filma na lestvici.
2. Program `csv_tabela.py` zbrane podatke zapiše v tabelo v '.csv' datoteko.
3. Program `tabela_st_glasov.py` ponovno ustvari '.csv' datoteko s tabelo, v kateri so le filmi z več kot 2 miljonoma oddanih glasov.
4. Program `ocene_po_letih.py` poišče povprčne ocene filmov iz vsakega desetletja in izriše graf rezultatov.
5. Program `top_filmi_desetletja.py` poišče naslov in oceno najbolje ocenjenega filma v vsakem desetletju in izriše časovnico.
6. Program `ocene_po_zanrih.py` poišče povprečne ocene filmov, glede na žanr, in izriše graf rezultatov. 
7. V datoteka `analiza.ipynb` so predstavljeni rezultati analize. 