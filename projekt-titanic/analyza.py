# Titanic – ANALÝZA
#
# Sem piš funkce, které něco spočítají a výsledek vrátí (return).
# Nepatří sem žádný input() ani print(), ty piš do zprava.py.
# Díky tomu půjdou funkce z tohohle souboru testovat.
#
# Začni krokem 1: cviceni/01_nacteni.md

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať ho spouštíš odkudkoliv.
SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"

def nacti_pasazery(SOUBOR):

    with open(SOUBOR, encoding="utf-8") as f:
        radky = list(csv.DictReader(f))
    return radky

def nazvy_sloupcu(pasazeri):
    zahlavi = []
    for i in pasazeri:
        zahlavi.append(i)
    return ", ".join(zahlavi)

def prvni_pasazer(pasazeri):
    pasazer = []
    for nazev, hodnota in pasazeri.items():
        pasazer.append(f"{nazev}: {hodnota}")
    return ", ".join(pasazer)


# ukol 2

def cislo_nebo_nic(text):
    if text == "":
        return None
    elif text.isdigit():
        cislo = float(text)
        return cislo
    else:
        return text

def uprav_pasazera(radek):
    pasazer = radek.copy()
    pasazer["Survived"] = int(radek["Survived"])
    pasazer["Pclass"] = int(radek["Pclass"])
    pasazer["SibSp"] = int(radek["SibSp"])
    pasazer["Parch"] = int(radek["Parch"])
    pasazer["Fare"] = float(radek["Fare"])
    pasazer["Age"] = cislo_nebo_nic(radek["Age"])
    return pasazer


def uprav_pasazery(radky):
    pasazeri = []
    for radek in radky:
        upraveny_pasazer = uprav_pasazera(radek)
        pasazeri.append(upraveny_pasazer)
    return pasazeri
