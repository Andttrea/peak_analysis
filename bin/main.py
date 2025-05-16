import os 
from genome import cargar_genoma, leer_archivos
from peaks import extraer_secuencias
from io_utils import guardar_fasta_por_tf
# Este script extrae secuencias FASTA de picos de unión de factores de transcripción.

def main():
    # Solicitar al usuario las rutas de los archivos

    print("Este script extrae secuencias FASTA de picos de unión de factores de transcripción.")

    archivo_genoma = os.path.join("data", "E_coli_K12_MG1655_U00096.3.txt")
    archivo_picos = os.path.join("data", "union_peaks_file.tsv")
    output_dir = os.path.join("results", "Archivos_Fasta")

    # Cargar el genoma y los picos
    genoma = cargar_genoma(archivo_genoma)
    picos = leer_archivos(archivo_picos)

    # Extraer las secuencias
    secuencias_por_tf = extraer_secuencias(picos, genoma)

    # Guardar las secuencias en archivos FASTA
    guardar_fasta_por_tf(secuencias_por_tf, output_dir)

# ejucion final del script
if __name__ == "__main__":
    main()

