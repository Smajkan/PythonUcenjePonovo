#Kreiraj varijablu koja je izvan funkcije i iskoristi je unutar funkcije

x = "zabavan"

def mojaFunkcija():
    x = "dobar"
    print("Python je " + x)
    
    
mojaFunkcija()

print("Python je " + x)