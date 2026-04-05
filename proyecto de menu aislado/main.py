import subprocess
import os

def limpiar():
    os.system("cls" if os.name=="nt" else "clear")
    
def ejecutar_nivel(nivel):
    resultado=subprocess.run(["docker", "run", "--rm", f"nivel_{nivel}"], capture_output=True, text=True)    
    if resultado.returncode ==0:
        print("\ncontraseña generada: ")
        print(resultado.stdout.strip())
    else:
        print("error al ejecutar docker")
        print(resultado.stderr)
        
    input("\npresiona ENTER para continuar... ")

def menu_prueba():
    while True:
        limpiar()
        print("""generador de contraseñas:\n. 
              1 - lv 1
              2 - lv 2
              3 - lv 3
              4 - lv 4
              5 - salir
              escoger un nivel de contraseña""")
        opcion=input("elija una opcion: ").strip()   
        if opcion=="1":
            ejecutar_nivel(1)
        elif opcion=="2":
            ejecutar_nivel(2)
        elif opcion=="3":
            ejecutar_nivel(3)
        elif opcion=="4":
            ejecutar_nivel(4)
        elif opcion=="5":
            break
        else:
            print("opción no válida")
            input("presiona ENTER para continuar... ")

if __name__ == "__main__":
    menu_prueba()