from registro import REGISTRO
def menu_user():
    while True:
        print(" WELCOME TO THE CHACHIPUN ")
        print("----------------------------------")
 
        print("1. Registrarme")
        print("2. Iniciar sesion")
        print("3.salir")

        elect=int(input("Que Opcion desea elegir: "))

        if elect==1 :
         nombre = input("INGRESE SU NOMBRE REAL: ")
         nickname = input("INGRESE SU NICKNAME : ")
         REGISTRO(nombre,nickname)
        elif elect==2:
         print("en proceso")
        elif elect == 3:
          print("ADIOS!!!")
          break
        else:
         print("ingrese una opcion valida")