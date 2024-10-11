lista_magos = ["Harry Houdini", "David Blaine", "Teller"]
lista_cientificos = ["Newton", "Hawking", "Einstein"]
lista_otros = ["Messi", "Pelé", "Juanes"]
lista_nombres = lista_magos + lista_cientificos + lista_otros

def hacer_grandioso():
    posicion=0
    for mago in lista_magos:
        lista_magos[posicion]="El Gran " + mago
        posicion = posicion + 1
        

def imprimir_nombres():
    for nombre in lista_nombres:
        print(nombre)

print("\nLista de Nombres:\n")
imprimir_nombres()

hacer_grandioso()

print("\nMagos Grandiosos:\n")
for mago in lista_magos:
    print(mago)
    
print("\nCientíficos:\n")
for cientifico in lista_cientificos:
    print(cientifico)
    
print("\nOtros:\n")
for otros in lista_otros:
    print(otros)

