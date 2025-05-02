"""

El siguiente código es un script que tiene como propósito automatizar 
la extracción de secuencias FASTA que corresponden a los picos de unión 
de factores de transcripción. Posteriormente guardaremos 
cada secuencia en un archivo FASTA separado. 

"""

import os #este es un modulo que nos va a ayudar a verificar si los directorios existen. Ya que interactua con el sistema operativo



def cargar_genoma(fasta_path): 
    """ Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto """

    if not os.path.isfile(fasta_path): #Con esto vamos a validar si el archivo existe
        print(f"El archivo de genoma no se encontró: {fasta_path}")
        exit(1) #Nos vamos a salir del programa 

    with open(fasta_path, 'r') as archivo_genoma:
        secuencia = "" # las comillas son para inicializar una variable como una cadena vacia
        secuencia = ''.join([linea.strip() for linea in archivo_genoma if not linea.startswith('>')]) #utilizamos comprensión de listas para limpiar la lista y vamos a concatenar en una sola con join
    return secuencia  


def leer_archivos(peaks_path):
    """ Lee el archivo de picos y va a devolver una lista de diccionarios con TF_name, start y end """
    
    if not os.path.isfile(peaks_path): 
        print(f"El archivo de picos no se encontró: {peaks_path}")
        exit(1)
    
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


def extraer_secuencias(peaks_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""

    secuencias_TF = {} #inicializamos en un diccionario vacio 
    for pico in peaks_data:
        TF_name = pico["TF_name"]
        start = pico["start"]
        end = pico["end"]

        secuencia = genoma[start-1:end] #vamos a extraer la secuencia del genoma 
         # le agregamos -1 porque el inicio es 1 y en python los indices empiezan desde 0


        # Verificamos si el TF_name ya existe en el diccionario
        if TF_name not in secuencias_TF:
            secuencias_TF[TF_name] = []
        secuencias_TF[TF_name].append(secuencia) #agregamos la secuencia  la lista de TF correspondiente
    
    return secuencias_TF


  

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guarda archivos FASTA separados por cada TF_name."""

    if not os.path.exists(output_dir): #verificamos si el directorio existe
        os.makedirs(output_dir) #si no existe lo creamos

    for TF_name, secuencias in secuencias_por_tf.items():  #items separa la clave y el valor
        nombre_archivo = os.path.join(output_dir, f"{TF_name}.fasta") #con os.path.join vamos a unir el directorio de salida con el nombre del archivo
        with open(nombre_archivo, 'w') as archivo_fasta:
            for i, secuencia in enumerate(secuencias):  
                archivo_fasta.write(f">{TF_name}_{i+1}\n") #vamos a escribir el encabezado del archivo fasta
                archivo_fasta.write(f"{secuencia}\n") # #escribimos la secuencia en el archivo fasta


def main():
    # Solicitar al usuario las rutas de los archivos
    print("Este script extrae secuencias FASTA de picos de unión de factores de transcripción.")
    print("Ingrese las rutas absolutas de los archivos que se piden a continuación.")
    archivo_genoma = input("Ruta archivo FASTA del genoma: ")
    archivo_picos = input("Ruta archivo de analisis de picos: ")
    output_dir = input("Ruta de salida de los archivos: ")

    # Cargar el genoma y los picos
    genoma = cargar_genoma(archivo_genoma)
    picos = leer_archivos(archivo_picos)

    # Extraer las secuencias
    secuencias_por_tf = extraer_secuencias(picos, genoma)

    # Guardar las secuencias en archivos FASTA
    guardar_fasta_por_tf(secuencias_por_tf, output_dir)

# ejucion final del script
main()





