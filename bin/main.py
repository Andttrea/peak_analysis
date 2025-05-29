import argparse
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

    # Agregando un parser para evitar el hardcoding - HJLO
    parser = argparse.ArgumentParser(description='Este script extrae secuencias FASTA de picos de unión de factores de transcripción.')
    parser.add_argument('-f', '--fasta', required=True, help='PATH del archivo FASTA')
    parser.add_argument('-p', '--peaks', required=True, help='PATH del archivo FASTA')
    parser.add_argument('-o', '--output', required=True, help='PATH del archivo FASTA')
    
    args = parser.parse_args()
    

    archivo_genoma = args.fasta
    archivo_picos = args.peaks
    output_dir = args.output

    # Cargar el genoma y los picos
    genoma = cargar_genoma(archivo_genoma)
    picos = leer_archivos(archivo_picos)

    # Extraer las secuencias
    secuencias_por_tf = extraer_secuencias(picos, genoma)

    # Guardar las secuencias en archivos FASTA
    guardar_fasta_por_tf(secuencias_por_tf, output_dir)

    # Mandar mensaje de exito - HJLO
    print(f'\n\nArchivos generados en: {args.output}')

# ejucion final del script
if __name__ == "__main__":
    main()

