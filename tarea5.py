def es_bisiesto(year):
    """
    Verifica si un año es bisiesto o no.
    
    Argumento:
    year -- Año que se desea verificar
    
    Retorna:
    True si el año es bisiesto, False si no lo es.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
year = int(input("digite el anio "))

if es_bisiesto(year):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")