import os
import pandas as pd

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
        return 0 #regresamos 0 para indicar que no se pudo cargar el genoma

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
      #Vamos a leer el archivo con pandas
    try:
        df = pd.read_csv(peaks_path, sep="\t") #leemos el archivo como un DataFrame
        if df.empty:
            print("ERROR: El archivo se encuentra vacio")
            return []
    except Exception as e:
        print(f"ERROR: No se pudo leer el archivo con pandas: {e}")
        return []

    #Procesamos el DataFrame para extraer la información necesaria
    lista_picos = []
    for index, row in df.iterrows():
        tf_name = str(row.iloc[1]).split(" ")[0]  #tomamos el nombre del TF de la segunda columna (Dataset IDs)
        peak_start = int(float(row.iloc[3]))      #convertimos de float a int (tercera columna)
        peak_end = int(float(row.iloc[4]))        #convertimos de float a int (cuarta columna)
        lista_picos.append({
            "TF_name": tf_name,
            "start": peak_start,
            "end": peak_end
        }) #guardamos la información en un diccionario y lo agregamos a la lista

    return lista_picos