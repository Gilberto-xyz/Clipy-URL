import random
import string

def generar_url(length=6):
    caracteres = string.ascii_letters + string.digits
    url_recortada = ''.join(random.choice(caracteres) for contador in range(length))
    return url_recortada
