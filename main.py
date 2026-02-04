import math

# Vypočet obsahu kruh

prumer_kruhu = 6 # průměr kruhu
zaokrouhleni_kruhu = 2 # zaokrouhleni na kolik desetinych míst pomocí round
obsah_kruhu = round(pow((prumer_kruhu / 2), 2) * math.pi, zaokrouhleni_kruhu)# výpočet kruhu pomocí: S = pi * r²

print("Obsah kruhu je: " + str(obsah_kruhu) + " a je zaokrouhlený na " + str(zaokrouhleni_kruhu) + " desetinná místa")
# print a je zde i napsáno na kolik desetinnych mist je to zaokrouhleé


# Vypočítání obvodu kruhu se stejnými veličinami

obvod_kruhu = round(math.pi * (prumer_kruhu / 2) * 2, zaokrouhleni_kruhu)
print("Obvod kruhu je: " + str(obvod_kruhu) + " a je zaokrouhlený na " + str(zaokrouhleni_kruhu) + " desetinná místa")

# Vypočet objemu krychl

# Výpočet povrchu kvádru

vyska_kvadr = 3 # veličiny stran
sirka_kvadr = 1 # veličiny stran
delka_kvadr = 7 # veličiny stran
povrch_kvadr = 2 * (vyska_kvadr * sirka_kvadr + sirka_kvadr * delka_kvadr + delka_kvadr * vyska_kvadr) # vypocet pomocí: 2 * (v * s + s * d + d * v)

print("Povrch kvádru je: " + str(povrch_kvadr)) # a zase výpis do programu

str_krychle = 4 # veličina strany
objem_krychle = pow(str_krychle, 3) # výpočet pro objem: a na 3

print("Objem krychle je: " + str(objem_krychle)) # print je výpis do konzole


# Výpočet 3 strany v trojúhelníku

a_troju = 6 # strana a
b_troju = 7 # strana b
zaok_troju = 4 # zaokrouhlení na kolik desetiných míst
c_troju = round(math.sqrt(pow(a_troju, 2) + pow(b_troju, 2)), zaok_troju) # vypocet pomoci: odmocniny a na 2 + b na 2 a zaokrouhleni celeho vypoctu

# round je zaokrouhlení, sqrt odmocnina, pow je stejné jak sqr takže mocnina
print("Strana c v trojúhelníku je: " + str(c_troju) + " a je zaokrouhlená na " + str(zaok_troju) + " desetinná místa") # zase print