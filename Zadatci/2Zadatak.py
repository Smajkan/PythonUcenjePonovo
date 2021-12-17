#Napraviti 2 varijable tipa string: x (gdje x ima vrijednost 2) i y (gdje y ima vrijednost nastavak) ispisati tip podataka obije varijable,
#Zatim napraviti 2 varijable tipa int br1 (gdje br1 ima vrijednost 4) i br2(gdje br2 ima vrijednost 10) ispisati tip podatka 
# obije varijable, a zatim odraditi spajanje stringa (string concacitation) nad varijablama x i y, a zatim i odraditi matematicku 
# operaciju sabiranja nad varijablama br_1 i br_2, a zatim ispisati rezultat spajanja stringa i matematicke operacije.
#Hint mozete a i ne morate iskoristiti casting
x=str('2')
y=str('nastavak')

print("Tip podatka varijable x je",type(x))
print("Tip podatka varijable y je",type(y))

br1, br2 = 4, 10

spajanje_str = x + y
rez = br1 + br2

print("Spajanje stringa: ", spajanje_str)
print("Rezultat matematicke operacije: ", rez)


