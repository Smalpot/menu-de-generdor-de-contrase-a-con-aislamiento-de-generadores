import secrets
import string

def generar_contrasena():
    letras=string.ascii_letters
    digitos=string.digits
    
    garantizados=[secrets.choice(digitos)]
    resto=[secrets.choice(letras+digitos) for _ in range(11)]
    
    contrasena=garantizados + resto
    import random
    random.shuffle(contrasena)
    print("".join(contrasena))
    
if __name__=="__main__":
    generar_contrasena()