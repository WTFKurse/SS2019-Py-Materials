def main():
	BASE_FEE = 0
	ELECTRICITY_PRICE = 0
	tariff = ""

	print("***************************************")
	print("Stromfix Rechner der Stadtwerke Dresden")
	print("***************************************\n")

	wastage = int(input("Dein Jahresstromverbrauch (in kWh):\t"))

	if(wastage <= 1500):
		tariff = "radio-lightning"
		BASE_FEE = 142.68
		ELECTRICITY_PRICE = 0.2412

	elif((wastage >= 1500) & (wastage < 3500)):
		tariff = "easy-green"
		BASE_FEE = 69.48
		ELECTRICITY_PRICE = 0.2292

	elif(wastage >= 3500):
		tariff = "electrical-short"
		BASE_FEE = 80.40
		ELECTRICITY_PRICE = 0.2235

	#printing data
	print("\nIhr passender Stromtarif lautet:")
	print("----------------------------------------------------")
	print(tariff)
	print("----------------------------------------------------\n")
	print("Tarifdaten")
	print("**************************")
	print("Grundpreis/Jahr in Netto:", BASE_FEE, "\b€.")
	print("Grundpreis/Jahr in Brutto:", BASE_FEE * 1.19, "\b€.")
	print("\nArbeitspreis/kWh in Netto:", ELECTRICITY_PRICE, "\b€.")
	print("Arbeitspreis/kWh in Brutto:", ELECTRICITY_PRICE * 1.19, "\b€.")



	#calculation
	netto = BASE_FEE + wastage * ELECTRICITY_PRICE
	brutto = netto * 1.19
	#printing result
	print("\nIhre jährlichen Kosten")
	print("**************************")
	print("Ihr Jahresverbrauch:", wastage, "\bkWh")
	print("Gesamtpreis (Netto) beträgt", netto, "\b€.")
	print("Gesamtpreis (Brutto)", brutto, "\b€.")



if __name__ == '__main__':
	main()
