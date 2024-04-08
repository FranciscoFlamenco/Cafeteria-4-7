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
    
    return True

# Pruebas utilizando pytest
def test_validar_entrada_bebida():
    
    # Casos de prueba válidos
    assert validar_entrada_bebida("Cafe,12,16,20,24") == True
    assert validar_entrada_bebida("Te,1") == True
    assert validar_entrada_bebida("Cerveza,10,20,30,40,48") == True
    assert validar_entrada_bebida("Cafe,1,2,3,4,5") == True
    assert validar_entrada_bebida("CafeNegro,48") == True

    # Casos de prueba inválidos
    assert validar_entrada_bebida("123,12,16,20,24") == False
    assert validar_entrada_bebida("C,12,16,20,24") == False
    assert validar_entrada_bebida("Cafe,0,16,20,24") == False
    assert validar_entrada_bebida("Cafe,12.5,16,20,24") == False
    assert validar_entrada_bebida("Cafe,12,16,20,15,24") == False
    assert validar_entrada_bebida("12,Cafe,16,20,24") == False
    assert validar_entrada_bebida("Cafe 12,16,20,24") == False