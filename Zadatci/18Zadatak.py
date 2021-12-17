#Potrebno je napisati program koji će provjeriti da li je godina prestupna ili ne. Program će uzimati kao input godinu, a kao output
# ukoliko je godina prestupna ispisivati: Prestupna godina, a ukoliko nije prestupna onda će ispisivati: "Nije prestupna godina"
#Da provjerimo da li je godina prestupna, moramo provjeriti sljedeće:
# 1) Ukoliko je godina djeljiva sa 4, onda trebamo ići na korak 2. Inače godina nije prestupna
# 2) Ukoliko je godina djeljiva sa 100, treba ići na korak 3, inače godina jeste prestupna.
# 3) Ukoliko je godina djeljiva sa 400, godina je prestupna, inače nije prestupna godina.


#Rješenje: 
year = int(input("Upišite godinu:"))

if year % 4 == 0:
    #Step2:
    if year % 100 == 0:
        #Step3
        if year % 400 == 0:
            print("Godina je prestupna")
        else:
            print("Godina nije prestupna")
    else:
        print("Godina je prestupna")
else:
    print("Godina nije prestupna")    
    