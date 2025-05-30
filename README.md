# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli

## 📋 Descripción del Proyecto

Este proyecto automatiza la extracción y análisis de secuencias genómicas donde los factores de transcripción se unen en *Escherichia coli*. El sistema procesa datos de experimentos ChIP-Seq para generar archivos FASTA específicos para cada factor de transcripción (TF) y facilitar el análisis posterior con herramientas como MEME.

## Objetivos Principales

1. **Extracción Automatizada**: Generar archivos FASTA individuales para cada factor de transcripción a partir de datos de picos de unión
2. **Análisis de Motivos**: Facilitar la identificación de motivos de unión mediante la automatización de comandos MEME
3. **Procesamiento Masivo**: Manejar datos de 144 factores de transcripción de forma eficiente

## Estructura del Proyecto

```
peak_analysis/
├── bin/                           # Scripts ejecutables
│   ├── extraccion_fasta.py       # Script monolítico (versión inicial)
│   └── extractor_secuencias/     # Módulo modularizado
│       ├── main.py               # Script principal
│       ├── genome.py             # Funciones de manejo del genoma
│       ├── peaks.py              # Procesamiento de picos
│       └── io_utils.py           # Utilidades de entrada/salida
├── data/                          # Datos de entrada
│   ├── union_peaks_file.tsv      # Archivo con información de picos
│   ├── E_coli_K12_MG1655_U00096.3.txt  # Genoma de E. coli
│   └── U00096.3.bfile            # Archivo de fondo para MEME
├── results/                       # Resultados generados
│   └── Archivos_Fasta/           # Archivos FASTA por TF
└── doc/                          # Documentación
    ├── detalles_proyecto.md      # Especificaciones técnicas
    ├── README_TF_Binding_Project.md  # Documentación del proyecto
    └── test_cases.md             # Casos de prueba
```

##  Funcionalidades Principales

### Módulo 1: Extractor de Secuencias FASTA

#### Funciones Principales

##### `cargar_genoma(fasta_path)`
- **Propósito**: Carga la secuencia completa del genoma desde un archivo FASTA
- **Parámetros**: 
  - `fasta_path` (str): Ruta al archivo FASTA del genoma
- **Retorna**: Secuencia del genoma como cadena de texto
- **Validaciones**: Verifica la existencia del archivo

##### `leer_archivos(peaks_path)`
- **Propósito**: Lee y procesa el archivo de picos TSV
- **Parámetros**:
  - `peaks_path` (str): Ruta al archivo TSV con datos de picos
- **Retorna**: Lista de diccionarios con información de picos
- **Formato de salida**:
  ```python
  [
      {
          "TF_name": "aaeR",
          "start": 3389342,
          "end": 3389658
      },
      ...
  ]
  ```
- **Validaciones**: 
  - Verifica existencia del archivo
  - Maneja archivos vacíos
  - Procesa formato TSV con pandas

##### `extraer_secuencias(peaks_data, genoma)`
- **Propósito**: Extrae secuencias genómicas basadas en coordenadas de picos
- **Parámetros**:
  - `peaks_data` (list): Lista de diccionarios con datos de picos
  - `genoma` (str): Secuencia completa del genoma
- **Retorna**: Diccionario con secuencias agrupadas por TF
- **Validaciones**: 
  - Verifica que las coordenadas estén dentro del rango del genoma
  - Maneja errores de rango

##### `guardar_fasta_por_tf(secuencias_por_tf, output_dir)`
- **Propósito**: Guarda archivos FASTA separados para cada factor de transcripción
- **Parámetros**:
  - `secuencias_por_tf` (dict): Diccionario con secuencias agrupadas
  - `output_dir` (str): Directorio de salida
- **Características**:
  - Crea el directorio de salida si no existe
  - Formato FASTA estándar con líneas de 75 caracteres
  - Nomenclatura: `{TF_name}.fasta`

### Formato de Datos de Entrada

#### Archivo de Picos (TSV)
El archivo de entrada contiene las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `Dataset_Ids` | Identificadores de experimentos | "aaeR inducible 1,aaeR inducible 2" |
| `TF_name` | Nombre del factor de transcripción | "aaeR" |
| `Peak_start` | Posición inicial del pico | 3389342.0 |
| `Peak_end` | Posición final del pico | 3389658.0 |
| `Peak_center` | Posición central del pico | 3389500.0 |
| `Peak_number` | Número secuencial del pico | 1 |
| `Max_Fold_Enrichment` | Enriquecimiento máximo | 68.21 |
| `Max_Norm_Fold_Enrichment` | Enriquecimiento normalizado | 1.0 |
| `Proximal_genes` | Genes próximos | "aaeR,tldD" |
| `Center_position_type` | Tipo de posición | "intergenic" |

## Uso del Sistema

### Instalación de Dependencias

```bash
pip install pandas argparse
```

### Ejecución del Extractor Modular

```bash
cd bin/extractor_secuencias/
python main.py -f /ruta/al/genoma.fasta -p /ruta/al/archivo_picos.tsv -o /directorio/salida/
```

### Parámetros de Línea de Comandos

- `-f, --fasta`: Ruta al archivo FASTA del genoma (requerido)
- `-p, --peaks`: Ruta al archivo TSV de picos (requerido)  
- `-o, --output`: Directorio de salida para archivos FASTA (requerido)

### Ejemplo de Uso Completo

```bash
# Extracción de secuencias FASTA
python main.py \
    -f ../../data/E_coli_K12_MG1655_U00096.3.txt \
    -p ../../data/union_peaks_file.tsv \
    -o ../../results/Archivos_Fasta/
```

## Resultados Esperados

### Archivos FASTA Generados
- Cada factor de transcripción genera un archivo individual
- Nomenclatura: `{TF_name}.fasta`
- Ejemplo de contenido:
```fasta
>aaeR_1
ATGCGTACGATCGTAGCTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGT
ACGATCGTACGATCGTACGATCGTACGATCGTACGATCGT
>aaeR_2
CGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACGATCGTACG
ATCGTACGATCGTACGATCGTACGATCGTACGATCGTACG
```

### Estadísticas del Proyecto
- **144 factores de transcripción** procesados
- **7,824 picos de unión** en total
- Archivos FASTA individuales por TF para análisis posterior

## Módulo 2: Automatización de MEME (Planificado)

### Objetivo
Generar scripts de shell para automatizar la ejecución de MEME en todos los archivos FASTA.

### Comando MEME Ejemplo
```bash
meme aaeR.fasta -oc aaeR_output/ -mod oops -nmotifs 1 -minw 14 -maxw 20 -bfile ../U00096.3.bfile -dna -maxsize 100000 -norand -seed 10
```

### Funcionalidad Planificada
- Lectura automática del directorio de archivos FASTA
- Generación de comandos MEME parametrizados
- Creación de script `run_meme.sh` ejecutable

## Manejo de Errores

### Validaciones Implementadas

1. **Archivo de Genoma No Encontrado**
   ```
   Error: El archivo de genoma no se encontró: /ruta/archivo.fasta
   ```

2. **Archivo de Picos Vacío**
   ```
   ERROR: El archivo se encuentra vacío
   ```

3. **Coordenadas Fuera de Rango**
   ```
   Error: El rango de los picos es de 1234567: 1234890
   Fuera del rango del genoma
   ```

4. **Formato de Archivo Inválido**
   ```
   ERROR: No se pudo leer el archivo con pandas: [detalle del error]
   ```

## Casos de Prueba

### Casos Implementados
1. Validación de existencia de archivos
2. Manejo de archivos vacíos
3. Verificación de coordenadas dentro del rango del genoma
4. Validación de formato de archivo de picos

## Tecnologías Utilizadas

- **Python 3.x**: Lenguaje principal
- **Pandas**: Procesamiento de datos TSV
- **argparse**: Manejo de argumentos de línea de comandos
- **os**: Operaciones del sistema de archivos

## Colaboración

### Control de Versiones
- Git para seguimiento de cambios
- Documentación completa del código
- Revisiones de código regulares

### Recursos Compartidos
- Secuencias FASTA de todos los TFs
- Archivo de genoma completo
- Scripts de automatización
- Repositorio GitHub para colaboración

## Buenas Prácticas Implementadas

1. **Modularización**: Separación de funcionalidades en módulos específicos
2. **Documentación**: Docstrings detallados en todas las funciones
3. **Validación**: Verificación robusta de datos de entrada
4. **Manejo de Errores**: Mensajes informativos y códigos de salida apropiados
5. **Parametrización**: Uso de argumentos de línea de comandos
6. **Formato Estándar**: Cumplimiento con estándares FASTA


## Contacto

**Desarrollador**: Andrea Villarruel García  
**Email**: andreavg@lcg.unam.mx  
**Fecha**: Marzo 2025

---

