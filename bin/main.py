import os 
from genome import cargar_genoma, leer_archivos
from peaks import extraer_secuencias
from io_utils import guardar_fasta_por_tf
# Este script extrae secuencias FASTA de picos de unión de factores de transcripción.
# Se espera que el usuario proporcione la ruta del archivo FASTA del genoma y el archivo de análisis de picos.
#Módulos necesarios:
# genome.py: contiene funciones para cargar_genoma() y leer_archivos()
# peaks.py: contiene la función extraer_secuencias()
# io_utils.py: contiene la función guardar_fasta_por_tf()

def main():
    """
    Función principal que orquesta todo el proceso:
    
    1. Define las rutas de los archivos de entrada y salida.
    2. Carga el genoma y los datos de los picos.
    3. Extrae las secuencias del genoma según las coordenadas de los picos.
    4. Guarda cada secuencia en archivos FASTA organizados por factor de transcripción.
    """


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

