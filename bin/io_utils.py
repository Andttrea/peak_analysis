import os

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