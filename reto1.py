#Programa Reto 1: Fundamentos de programación Curso 51659
from os import system
system("cls")
print(f"Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Se crean las variables usuario y contraseña predeterminadas
usuario=int(51659)
clave=95615
dato_usuario=int(input("Digite usuario: "))#Solicitamos que digite el usuario y verificamos si es correcto
if dato_usuario == usuario:
    dato_clave=int(input("Digite Contraseña: "))#Despues de verificar que si es el usuario solictaremos la contraseña y verificamos si es correcta
    if dato_clave == clave:
        captcha_2=int((((9*5)-(6*5))/5)+1+1) #Creacion de la segunda parte del Captcha con operaciones
        print(f"659 +", captcha_2 ,"=") # Se muestra en pantalla
        suma=int(input("Digite resultado de la suma: "))#Solicitamos al usuario que difite el valor de la suma
        if suma == 664: #se verifica si el captcha fue resuelto 
            print("Sesión iniciada")
        else:
            print("Error") #Error al digitar mal el valor del captcha
    else:
        print("Error")#Error al digitar mal la contraseña
else:
    print("Error")#Error al digitar mal el usuario