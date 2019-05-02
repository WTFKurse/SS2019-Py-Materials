 while True:

        try:
            verbrauch = input("Bitte geben Sie Ihren Verbrauch in kWh ein!\n")
            verbrauch = int(verbrauch)
            break

        except ValueError:
            print("Das war kein Integer du Schlawiner!")

  print("Super! Danke für deine mitarbeit.\n")
