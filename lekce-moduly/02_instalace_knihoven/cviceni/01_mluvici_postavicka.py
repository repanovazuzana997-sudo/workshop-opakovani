# Cvičení 1 – Mluvící postavička
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatelky, co má postavička říct a která to má být
#    (třeba cow, tux nebo dragon). Pak ji nech promluvit.
#
#    cowsay.draw(text, cowsay.CHARS[jmeno]) nechá mluvit postavičku
#    podle jména. Seznam jmen je v cowsay.char_names. Když jméno
#    v seznamu není, vypiš, ze kterých jde vybírat.

import cowsay

co_rict = input("Co říká postavička?")
jmeno = input("Která postavička?").strip().lower()

if jmeno in cowsay.char_names:
    cowsay.draw(co_rict, cowsay.CHARS[jmeno])
else:
    print("Takovou neznám. Vyber si z:", ", ".join(cowsay.char_names))
