# Titanic – ZPRÁVA
#
# Tenhle soubor spouštíš (Run). Volá funkce z analyza.py a vypisuje
# výsledky. Patří sem všechno s print() a input().
#
# Začni krokem 1: cviceni/01_nacteni.md

import analyza


print("Titanic")
print(f"Data jsou v souboru {analyza.SOUBOR.name}.")

pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)


print(f"Počet pasažerů je {len(pasazeri)}.")
print("Názvy sloupců: ", analyza.nazvy_sloupcu(pasazeri[0]))
print("První pasažér je:", analyza.prvni_pasazer(pasazeri[0]))



pasazeri = analyza.uprav_pasazery(pasazeri)


