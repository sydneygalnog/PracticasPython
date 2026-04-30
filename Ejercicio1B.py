# %%
lista_temp=[("Acapulco",33),("CDMX", 26),("Monterrey", 34)]

#generador de datos
def leer_temperaturas(l):
    for i in l:
        yield i

# %%
for i in leer_temperaturas(lista_temp):
    print(i)

# %%
#Filtrado con filter() y lambda
filtro_temperatura=list(filter(lambda x:x[1]>=30,lista_temp))
print(filtro_temperatura)

# %%
#Transformación con map & lambda
lista_alerta=list(map(lambda x:"Alerta de calor en "+ x[0]+": "+str(x[1])+" °C",filtro_temperatura))
print(lista_alerta)

# %%
#Ordenamiento con sorted() y key=lambda
lista_ordenada=sorted(filter(lambda x:x[1]>=30,lista_temp),key= lambda x: x[1],reverse=True)
print(lista_ordenada)

# %%
#reduce
from functools import reduce
suma_temp=reduce(lambda x,y:x+y[1],filtro_temperatura,0)
promedio=suma_temp/len(filtro_temperatura)
#print(suma_temp)
print(promedio)

# %%
#decorador personalizado
def decorador_personalizado(funcion):
    def funcion_modifica():
        funcion_modifica.contador+=1
        funcion()
        print(f"Nombre de la funcion: {funcion.__name__}")
        print(f"Veces que se llamo a la funcion: { funcion_modifica.contador}")
    funcion_modifica.contador=0
    return funcion_modifica

# %%
@decorador_personalizado
def saludo():
    print("Hola mundo:)))")

saludo()

# %%
saludo()

# %%
#usando el decorador de medir tiempo
#Agregando las lineas dentro del decorador personalizado
import time
def decorador_personalizado(funcion):
    def funcion_modifica():
        inicio=time.time()
        funcion_modifica.contador+=1
        funcion()
        fin=time.time()
        print(f"Nombre de la funcion: {funcion.__name__}")
        print(f"Veces que se llamo a la funcion: { funcion_modifica.contador}")
        print(f"Tiempo: {fin-inicio:.4f} segundos")
    funcion_modifica.contador=0
    return funcion_modifica


# %%
#llamar nuevamente al decorador que se modifico
@decorador_personalizado
def saludo():
    print("Hola mundo:)))")

saludo()

# %%
saludo()

# %%
#Salida final
for i in lista_alerta:
    print(i)
print(f"Temperatura promedio de alertas {promedio}")

# %%



