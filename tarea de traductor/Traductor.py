def cargar_traducciones(archivo):
    traducciones = {}
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
                palabra_ingles, palabra_espanol = linea.strip().split('=')
                traducciones[palabra_ingles.lower()] = palabra_espanol.lower()
                traducciones[palabra_espanol.lower()] = palabra_ingles.lower()
    except FileNotFoundError:
        pass
    return traducciones

def guardar_traducciones(archivo, traducciones):
    with open(archivo, 'w', encoding='utf-8') as file:
        for palabra_ingles, palabra_espanol in traducciones.items():
            file.write(f"{palabra_ingles}={palabra_espanol}\n")

def agregar_traduccion(traducciones, palabra_ingles, palabra_espanol):
    traducciones[palabra_ingles.lower()] = palabra_espanol.lower()
    traducciones[palabra_espanol.lower()] = palabra_ingles.lower()

def traducir(traducciones, codigo, palabra):
    idioma_origen, idioma_destino = codigo.split('-')
    
    if idioma_origen == 'EN' and idioma_destino == 'ES':
        traduccion = traducciones.get(palabra.lower())
    elif idioma_origen == 'ES' and idioma_destino == 'EN':
        for key, value in traducciones.items():
            if value == palabra.lower():
                traduccion = key
                break
        else:
            traduccion = None
    else:
        return "Código de idioma no válido. Use 'EN-ES' o 'ES-EN'."

    if traduccion:
        return f"{codigo} {palabra} --> {traduccion}"
    else:
        return f"Traducción no encontrada para {codigo} {palabra}"

archivo_traducciones = "EN-ES.txt"
traducciones = cargar_traducciones(archivo_traducciones)

while True:
    print("\nMenú:")
    print("1. Agregar nueva traducción")
    print("2. Traducir")
    print("3. Salir")
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        palabra_ingles = input("Ingrese la palabra en inglés: ")
        palabra_espanol = input("Ingrese la traducción en español: ")
        agregar_traduccion(traducciones, palabra_ingles, palabra_espanol)
        guardar_traducciones(archivo_traducciones, traducciones)
        print("Traducción agregada correctamente.")
    elif opcion == '2':
        codigo = input("Ingrese el código de idioma (EN-ES/ES-EN): ")
        palabra = input("Palabra a traducir: ")
        resultado = traducir(traducciones, codigo.upper(), palabra)
        print(resultado)
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Intente nuevamente.") 