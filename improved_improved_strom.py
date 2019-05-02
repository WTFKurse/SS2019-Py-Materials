def main():
    while True:
        verbrauch = input("Bitte ihren Verbrauch eingeben.\n")
        try:
            verbrauch = int(verbrauch)
            if verbrauch > 0:
                break
            else:
                print("Negativer Verbrauch muss in einem Extre Vertrag geregelt werden\n")
        except ValueError:
            print("Das war leider keine Zahl.\n")

    switch = {
        1: tarif1,
        2: tarif2,
        3: tarif3
    }

    if verbrauch < 1500:
        switch[1](verbrauch)
    elif 1500 <= verbrauch <= 2500:
        switch[2](verbrauch)
    elif verbrauch >= 2500:
        switch[3](verbrauch)


def tarif1(verbrauch):
    grundpreis_netto = 142.68
    arbeitspreis_netto = 0.2412

    ausgabe(verbrauch, grundpreis_netto, arbeitspreis_netto)


def tarif2(verbrauch):
    grundpreis_netto = 142.68
    arbeitspreis_netto = 0.2412

    ausgabe(verbrauch, grundpreis_netto, arbeitspreis_netto)


def tarif3(verbrauch):
    grundpreis_netto = 142.68
    arbeitspreis_netto = 0.2412

    ausgabe(verbrauch, grundpreis_netto, arbeitspreis_netto)


def ausgabe(verbrauch, grundpreis_netto, arbeitspreis_netto):
    gesamtkosten_netto = grundpreis_netto + (verbrauch * arbeitspreis_netto)
    gesamtkosten_brutto = gesamtkosten_netto * 1.19
    print(f"Sie haben den ersten Tarif, da ihr Verbrauch bei {verbrauch}kWh liegt.\nBrutto: {gesamtkosten_brutto}€\nNetto: {gesamtkosten_netto}€")


if __name__ == '__main__':
    main()
