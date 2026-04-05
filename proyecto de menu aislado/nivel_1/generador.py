import secrets
import string

def generar_contrasena():
    caracteres=string.ascii_lowercase
    contraseña="".join(secrets.choice(caracteres)for _ in range(10))
    print(contraseña)
    
if __name__=="__main__":
    generar_contrasena()