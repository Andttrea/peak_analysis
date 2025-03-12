### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA


1.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
2.  **Caso: Archivo de picos vacío.**
    
    -   **Entradas:**
        -   Archivo de picos vacío.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the peak file is empty."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
```

3.  **Caso: Posiciones `Peak_start` y `Peak_end` fuera del rango del genoma.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` fuera del tamaño del genoma.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks are bigger than the genome". Check the log.out file`
        
        -   Generar un archivo de log indicando los picos fuera de rango. El archivo debe contener las líneas del archivo de picos que tienen problemas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls
```

```bash
log.out
fasta_peaks/
```

4. **Caso: Formato incorrecto en el archico de picos**

   - **Entradas**
   - Archivo de picos con un formato incorrecto (columnas faltantes o vacías).
   - Archivo FASTA del genoma válido.
   - Directorio de salida.
     
   - **Esperado**
   - Nuestro sistema debe de imprimir el siguiente mensaje: `"Error: Formato peak file inválido"`


     ```python
         mk_fasta_from_peaks.py -i malformed_peak_ file.txt -g Ecoli.fna -o fasta_peaks/
     ```

     ```
     Error: Formato peak file inválido

     ```

     5. ** Caso: Permisos insuficientes para escribir en el directorio de salida **

     - **Entradas**
     - Archivo de picos válido.
     - Archivo FASTA del genoma válido.
     - Directorio de salida sin permisos de escritura.

     - **Esperado**
     - Nuestro sitema debe de imprimir el siguiente mensaje: `"Error: No se puede escribir al directorio de salida"`
    
     ```python
         mk_fasta_from_ peaks.py -i peak_file.txt -g Ecoli.fna -o /protected_dir/
     ```

     ```
       Error: No se puede escribir al directorio de salida

     ```
