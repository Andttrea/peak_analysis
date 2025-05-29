def extraer_secuencias(peaks_data, genoma):
    """
    En esta función agrupamos las secuencias extraídas por TF_name en un diccionario.

    Parametros:
    peaks_data: lista de diccionarios con la información de los picos
    genoma: secuencia del genoma

    Retorna:
    secuencias_TF: diccionario con las secuencias agrupadas por TF_name
"""

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
