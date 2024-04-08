#Se utiliza expresiones regulares para validar el nombre
# Francisco Flamenco Andrade A01732742
import re

def validar_entrada_bebida(entrada):
    # Eliminar espacios en blanco de la entrada
    entrada = entrada.replace(" ", "")
    
    # Dividir la entrada en nombre y tamaños separados por coma
    partes = entrada.split(",")
    
    # Validar que haya al menos dos partes (nombre y tamaños)
    if len(partes) < 2:
        return False
    
    # Validar el nombre de la bebida
    nombre_bebida = partes[0]
    # Se utiliza la funcion match de la libreria re, para asegurar que el nombre sea correcto
    if not re.match("^[a-zA-Z]{2,15}$", nombre_bebida):
        return False
    
    # Validar los tamaños de la bebida
    tamanos = partes[1:]
    if len(tamanos) > 5:
        return False
    
    ultimo_tamano = 0
    for tamano_str in tamanos:
        try:
            tamano = int(tamano_str)
        except ValueError:
            return False
        
        if tamano <= ultimo_tamano or tamano < 1 or tamano > 48:
            return False
        
        ultimo_tamano = tamano
    #Si todo cumple, regresa True
    return True
