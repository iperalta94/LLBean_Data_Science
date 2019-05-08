# ejemplo de listas

# crear una lista de 4 numeros

a = [87, 54, 94, 11]
print(a)

#agregar un elemento

a.append(2)
print(a)
#agregar 2 elementos al mismo tiempo

a.extend([8,9])
print(a)

print("esta es la lista",a)

print(a[1:-1])

#salto
#los elementos pares

print(a[::2])

#los elementos impares
print(a[1::2])

edad=17
if edad < 18:
    print("Menor")
else:
    print("Mayor")

pixel= [0.6,0.3,0.4]
suma=sum(pixel)
n=len(pixel)
intensidad=suma/n # IMPLEMENTAR

print("La intensidad es:")
print(intensidad)

#otrasolucion ciclo
p=0
for numero in pixel:
    p += numero

instensidad2 = p/len(pixel)
print("a",instensidad2)

#tercera solucion
mi_suma=sum(pixel)
mi_promedio= mi_suma/len(pixel)

print("El Pixel es")

if intensidad > 0.5:
    print("Blanco")
else:
    print("Negro")

lista=[44,11,15,29,53,12,30]
maximo=0
for s in lista
    maximo=
    print(maximo)