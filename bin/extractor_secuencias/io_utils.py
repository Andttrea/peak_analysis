import os

def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """
    Guarda archivos FASTA separados por cada TF_name.

    Parametros:
    secuencias_por_tf: diccionario con las secuencias agrupadas por TF_name
    output_dir: directorio de salida donde se guardarán los archivos FASTA

    """

    if not os.path.exists(output_dir): #verificamos si el directorio existe
        os.makedirs(output_dir) #si no existe lo creamos

    for TF_name, secuencias in secuencias_por_tf.items():  #items separa la clave y el valor
        nombre_archivo = os.path.join(output_dir, f"{TF_name}.fasta") #con os.path.join vamos a unir el directorio de salida con el nombre del archivo
        with open(nombre_archivo, 'w') as archivo_fasta:
            for i, secuencia in enumerate(secuencias):  #aquí enumeramos las secuencias para tener un índice
                archivo_fasta.write(f">{TF_name}_{i+1}\n") #vamos a escribir el encabezado del archivo fasta, sumamos 1 al índice para que empiece desde 1
                # Dividir la secuencia en líneas de 75 caracteres máximo
                for j in range(0, len(secuencia), 75):
                    archivo_fasta.write(f"{secuencia[j:j+75]}\n") #escribimos la secuencia en líneas de 75 caracteres