import secrets
import string

def generar_contrasena():
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    garantizados = [
        secrets.choice(mayusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(simbolos)
    ]

    caracteres = mayusculas + minusculas + digitos + simbolos
    resto = [secrets.choice(caracteres) for _ in range(16)]

    contrasena = garantizados + resto
    contrasena = list(contrasena)
    secrets.SystemRandom().shuffle(contrasena)
    print("".join(contrasena))

if __name__ == "__main__":
    generar_contrasena()