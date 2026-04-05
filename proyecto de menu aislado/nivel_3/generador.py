import secrets
import string

def generador_contrasena():
    letras=string.ascii_letters
    digitos=string.digits
    simbolos=string.punctuation
    
    garantizados=[
        secrets.choice(letras),
        secrets.choice(digitos),
        secrets.choice(simbolos)
    ]
    
    caracteres=letras+digitos+simbolos
    resto=[secrets.choice(caracteres) for _ in range(13)]
    
    contrasena=garantizados+resto
    contrasena=list(contrasena)
    secrets.SystemRandom().shuffle(contrasena)
    print("".join(contrasena))
    
if __name__=="__main__":
    generador_contrasena()
    
    
    