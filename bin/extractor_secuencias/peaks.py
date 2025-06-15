def extraer_secuencias(peaks_data, genoma):
    """
    En esta función agrupamos las secuencias extraídas por TF_name en un diccionario.

    Parametros:
    peaks_data: lista de diccionarios con la información de los picos
    genoma: secuencia del genoma

    Retorna:
    secuencias_TF: diccionario con las secuencias agrupadas por TF_name
    """

    longitud_genoma = len(genoma) #vamos a ver cuando mide nuestro genoma 

    secuencias_TF = {} #inicializamos en un diccionario vacio 
    for pico in peaks_data:
        TF_name = pico["TF_name"]
        start = pico["start"]
        end = pico["end"]

        #Vamos verificar si peak start y peak end no estan fuera del rango del genoma
        if start < 1 or end > longitud_genoma:
            print(f"Error: El rango de los picos es de {start}: {end}")
            print("n/Fuera del rzango del genoma")
            return 0 
           
        
        secuencia = genoma[start-1:end] #el slicing inicia en 0, por eso restamos 1 al start

        # Verificamos si el TF_name ya existe en el diccionario
        if TF_name not in secuencias_TF:
            secuencias_TF[TF_name] = [] # Si no existe, inicializamos una lista vacía para ese TF_name
        secuencias_TF[TF_name].append(secuencia) #agregamos la secuencia  la lista de TF correspondiente
    
    return secuencias_TF
