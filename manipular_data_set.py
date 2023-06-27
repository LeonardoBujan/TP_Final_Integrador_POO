import pandas as pd
import numpy as np

def limpiar_data_set(data_frame):        

    # Variable diccionario que contiene el nombre de las columnas a renombrar en el data set
    renombrar_columnas = {"lat":"latitud", "lng":"longitud", "licitacion_oferta_empresa":"empresa", "cuit_contratista":"cuit", "expediente-numero": "expediente_numero"}

    # Actualización del data set con el nuevo nombre de columnas definidos en el diccionario
    data_frame = data_frame.rename(columns=renombrar_columnas)

    # Variable lista que contiene el nombre de las columnas que van a ser eliminadas en el data set
    eliminar_columnas = ["imagen_2","imagen_3","imagen_4","beneficiarios","compromiso","ba_elige","pliego_descarga","estudio_ambiental_descarga"]

    # Actualizacion del data set con las columnas que van a quedar en la exploracion de datos
    data_frame = data_frame.drop(columns=eliminar_columnas)

    # Variable diccionario que contiene el nombre de las columnas para las cuales se va a modificar el valor nulo por otro en el data set
    actualizar_columnas_nan = {"destacada": "Sin determinar", "financiamiento": "Sin asignar", "expediente_numero": "Sin expediente"}

    # Actualizacion del data set con las columnas que van a quedar en la exploracion de datos
    data_frame = data_frame.fillna(value=actualizar_columnas_nan)

    # Actualiza el data set quitando los registros que contienen celdas vacías
    data_frame = data_frame.dropna()

    # Actualiza el data set eliminando los registros duplicados
    data_frame = data_frame.drop_duplicates()

    return data_frame