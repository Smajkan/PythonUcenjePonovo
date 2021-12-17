#Izračunati vrijednosti prema izrazima:
#  a = x * y
#  b = x + y
#  c = b / x

x = float(input("Unesite vrijednost x: "))
y = float(input("Unesite vrijednost y: "))

print("1) a=",x,"*",y)
print("2) b=",x,"+",y)
print("3) c=",x,"/",y)
print("--------------")
a = x*y
b = x+y
if(x<y):
    print("a = ",a)
    print("b = ",b)
    print("c nije bilo moguce izracunati iz razloga sto je vrijednost x manja od y")
else:
    c = x/y
    print("a = ",a)
    print("b = ",b)
    print("c =",c)
    


