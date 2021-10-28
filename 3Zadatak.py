#Da li ste se ikada zapitali koliko ima sekundi u mjesecu (ukoliko uzmemo u obzir da mjesec ima 30 dana)?
#Ukoliko jeste ili ipak niste, napišite program koji će izračunati koliko ima sekundi u mjesecu i ispišite rezultat

sati_u_jednom_danu = 24
sekundi_u_jednom_satu = 3600

dani_u_jednom_mjesecu= 30

ukupno_sekundi_u_danu = sati_u_jednom_danu * sekundi_u_jednom_satu

ukupno_sekundi_u_mjesecu = dani_u_jednom_mjesecu * ukupno_sekundi_u_danu
print("U jednom mjesecu ima sekundi: ", ukupno_sekundi_u_mjesecu)
