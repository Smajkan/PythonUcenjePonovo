#Potrebno je da izračunate ukupno vrijeme leta za nadolazeće putovanje.
#Letite iz Los Angelesa do Sydney-a čija udaljenost iznosi 7425 milja. Avion leti prosječnom brzinom od 550 milja po satu.
#Izračunajte i ispišite ukupno vrijeme leta u satima
#HINT: Rezultat bi trebao biti float

udaljenost = 7425 #milja
prosjecna_brzina = 550 #milja/h

# v = s/t (s - pređeni put ; t - vrijeme ; v - brzina kretanja) t = s/v
vrijeme =  udaljenost / prosjecna_brzina
print(vrijeme)