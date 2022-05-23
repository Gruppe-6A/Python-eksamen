# Black Jack Assistant

Black jack assistent, hjælper dig med at vælge om du skal 'hit' eller 'stand'.
Programmet tager et billede af et spil blackjack som input.
Her vil programmet forstå de øverste kort som værende dealerens kort og de nederste kort som værende spillernes kort.

OBS: Billederne skal helst tages på en sort baggrund

![Eksempel](Card_Imgs/DetFirstHand.jpg "Eksempel")

## Teknologier

- Pip (21.2.4)
- Python 3 (3.7.6)
- OpenCV (4.5.5)
- Numpy (1.18.5)
- MatPlotLib (3.2.1)
- Pytesseract (0.3.9)
- Jupyter Notebooks (6.0.3)

## Installations Guide

### Jupyter Notebooks

For at installere de biblioteker vi bruger, skal du bare køre den øverste celle, inde i `read_images.ipynb`

### Python 3

Kopier følgende ind i din terminal

```sh
pip install opencv-python, pytesseract, numpy, matplotlib
```

## Kom i gang

Du kan enten benytte Jupyter Notebooks eller køre det som python projekt i en IDE.

### Jupyter Notebooks

For at komme i gang, skal du til at starte med at `git clone` projektet, til der hvor du har din egen Jupyter Notebook.
Upload billedet som du vil bruge til `Card_Imgs` folderen eller brug et af dem der allerede er der.
Inde i `read_images.ipynb` skal du ændre `name_of_picture.jpg`.

Det er inde i denne funktion:

`input_img = cv2.imread('Card_Imgs/name_of_picture.jpg', 1)`

### Python fil

For at komme i gang skal du `git clone` projektet til dit skrivebord.
Derefter kører du filen ved at skrive `python read_images.py hand1.jpg` i din terminal.
Her er `hand1.jpg` navnet på det billede, som du gerne vil bruge.

## Hvad har i nået/ikke nået

Vi har taget billeder af fysiske spillekort, og så derefter sat dem ind i en mappe.
Vi henter så billederne fra mappen og bruger OpenCV til at lave billedemanipulation, så vi nemmere kan benytte Tesseract til at finde kortenes værdi.
Udover dette, har vi lavet en algoritme der ved brug af blackjack statistik kan udregne hvad det optimale næste træk er.
Algoritmen tager kortenes værdi som input og fortæller spilleren hvorvidt de skal 'stand' eller 'hit.

## Liste af udfordringer

- Tesseract har problemer med enkelte tal, specifikt 3 & 10.
- Problemer med at warpe/beskære billederne, så de kan læses af Tesseract.
- At skrive en algoritme, der udregner om du skal 'hit' eller 'stand'.
