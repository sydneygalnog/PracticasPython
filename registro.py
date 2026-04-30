#Función: validar datos
#Parametros:
#  nombre -> tipo cadena
#  edad ->  tipo entero
#  correo -> tipo cadena
# *No tiene retorno, más si funciona para crear las excepciones especificas y un mensaje de las mismas
# excepciones: cadena vacia en nombre, que no exista el caracter arroba en correo, que nombre y correo no sean de tipo cadena, etc
def validar_datos(nombre, edad, correo):
    validar_cero=100/edad
    #validar que la cadena de texto no sea vacia
    if nombre=="":
        raise ValueError("Cadena de texto vacia")
    
    #valida que exista arroba en la cadena del correo
    if "@" not in correo:
        raise ValueError("No existe arroba")
    #validaciones de tipo
    if not isinstance(nombre,str) or not isinstance(correo,str):
        raise TypeError("Nombre o correo no son de tipo texto")
    
    if not isinstance(edad,int):
        raise TypeError("Edad no es un dato numerico tipo entero")
    #valida que la edad sea mayor que cero
    if edad<0:
        raise ValueError("Edad es negativa")

#Función: probar validaciones
#Parametros:
#  nombre -> tipo cadena
#  edad ->  tipo entero
#  correo -> tipo cadena
# *No tiene retorno
# Tiene un bloque try, excep y finally para iniciar la validacion (llama a la funcion validar datos) y cachar los errores
def probar_validaciones(nombre,edad,correo):
    try:
        print("Validando datos...")
        print("Datos a validar:")
        print(f"-Nombre: {nombre}\n-Edad: {edad}\n-Correo: {correo}")
        validar_datos(nombre,edad,correo)
        print("Resultado de validación-> Datos correctos:)")
    
    except ZeroDivisionError:
        print("Resultado de validación-> Ocurrio un error: La edad es cero")
    except Exception as e:
        print(f"Resultado de validación-> Ocurrio un error: {e}")
    
    finally:
        print("Se termino la validación")


probar_validaciones("sydney",0,"sydzac@hotmail")
probar_validaciones("Moises",31,"moisesmg@hotmail.com")
probar_validaciones("silvia",-40,"nngd@gmail.com")
probar_validaciones(21,35,"veintiuno@outlook.com")
probar_validaciones("jose",45,"josemaderohotmail.com")