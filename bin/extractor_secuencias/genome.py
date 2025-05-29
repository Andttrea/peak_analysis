import os

def cargar_genoma(fasta_path): 
    """
    Carga la secuencia del genoma desde un archivo FASTA y la devuelve como una única cadena de texto.
    
    Parámetros:
    fasta_path: Ruta al archivo FASTA del genoma.
    
    Retorna:
    secuencia: Secuencia del genoma concatenada sin encabezados ni espacios.

    """

    if not os.path.isfile(fasta_path): #Con esto vamos a validar si el archivo existe
        print(f"El archivo de genoma no se encontró: {fasta_path}")
        exit(1) #Nos vamos a salir del programa 

    with open(fasta_path, 'r') as archivo_genoma:
        secuencia = "" # las comillas son para inicializar una variable como una cadena vacia
        secuencia = ''.join([linea.strip() for linea in archivo_genoma if not linea.startswith('>')]) #utilizamos comprensión de listas para limpiar la lista y vamos a concatenar en una sola con join
    return secuencia  


def leer_archivos(peaks_path):
    """
    Lee el archivo de picos y va a devolver una lista de diccionarios con TF_name, start y end
   
    Parámetros:
    peaks_path (str): Ruta al archivo TSV de picos.
    
    Retorna:
    list of dict: Lista de diccionarios. Cada diccionario contiene:
                  - "TF_name": Nombre del factor de transcripción
                  - "start": Posición de inicio del pico 
                  - "end": Posición de fin del pico
    """
    
    if not os.path.isfile(peaks_path): 
        print(f"El archivo de picos no se encontró: {peaks_path}")
        return 0 
    
    lista_picos = [] #vamos a inicializar una lista vacia
    with open(peaks_path, 'r') as archivo_picos: 
        archivo_picos.readline() #esto va a saltar el encabezado 
        for linea in archivo_picos:
            valores = linea.strip().split("\t")
            TF_name = valores[1].split(" ")[0] #esto va a tomar el nombre del TF que esta en Dataset IDs
            peak_start = int(float(valores[3])) #convertimos de float a int porque en el archivo vienen todos los valores con .0 
            peak_end = int(float(valores[4]))
            lista_picos.append({   #este va a ser nuestro diccionario
                "TF_name": TF_name,
                "start": peak_start,
                "end": peak_end
            })

    return lista_picos 