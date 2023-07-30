from random import choice


def generarPassword(longitud: int, upperCase: bool, numbers: bool, simbols: bool) -> str:
    caracteres = [chr(k) for k in range(97, 123)]

    caracteres += [chr(k) for k in range(65, 91)] if upperCase else []
    caracteres += [str(k) for k in range(10)] if numbers else []
    caracteres += [chr(k) for k in range(33, 48)] + [chr(k)
                                                     for k in range(58, 65)] + [chr(k) for k in range(91, 97)] if simbols else []

    password = ''

    for k in range(longitud):
        password += choice(caracteres)

    return password


print(generarPassword(16, True, True, True))
