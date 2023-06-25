from abc import ABC, abstractmethod
from peewee import *
import pandas as pd
from modelo_orm import *
from directorio import *
from manipular_data_set import *

class GestionarObra(ABC):
    
    @classmethod
    def extraer_datos(cls):
        path_completo = f"{obtener_directorio()}/observatorio-de-obras-urbanas.csv"
        archivo_csv = path_completo
        try:
            df = pd.read_csv(archivo_csv, sep=",")
            return df
        except FileNotFoundError as e:
            print(f"Error al conectar el dataset {e}")
            return False

    @classmethod
    def conectar_db(cls):        
        try:
            return sqlite_db.connect()
        except OperationalError as e:
            print(f"Error al conectar con la BD. {e}")
            exit()

    @classmethod
    def mapear_orm(cls):
        try:            
            # Creamos las tablas correspondientes a las clases del modelo
            sqlite_db.create_tables([Entorno, Etapa, Tipo, AreaResponsable, Comuna, Barrio,
                        LicitacionAnio, Empresa, Obras])
        except OperationalError as e:
            print(f"Error al crear la estructura de la BD. {e}")

    @classmethod
    def limpiar_datos(cls, data_frame):
        df = limpiar_data_set(data_frame)
        return df

    @classmethod
    def cargar_datos(cls, data_frame):
        lista_entorno = list(data_frame["entorno"].unique())
        for elem in lista_entorno:
            try:
                Entorno.create(nombre_entorno=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla enotornos. {e}")
        print("Se han persistido los tipos de entornos en la BD.")

        lista_etapa = list(data_frame["etapa"].unique())
        for elem in lista_etapa:
            try:
                Etapa.create(nombre_etapa=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla etapas. {e}")
        print("Se han persistido las etapas de las obras en la BD.")

        lista_tipo_obra = list(data_frame["tipo"].unique())
        for elem in lista_tipo_obra:
            try:
                Tipo.create(nombre_tipo=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla enotorno. {e}")
        print("Se han persistido los tipos de obras en la BD.")

        lista_area_responsable = list(data_frame["area_responsable"].unique())
        for elem in lista_area_responsable:
            try:
                AreaResponsable.create(area_responsable=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla areas_responsable. {e}")
        print("Se han persistido las areas responsables en la BD.")

        lista_comuna = list(data_frame["comuna"].unique())
        for elem in lista_comuna:
            try:
                Comuna.create(nombre_comuna=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla comunas. {e}")
        print("Se han persistido las comunas en la BD.")

        lista_barrio = list(data_frame["barrio"].unique())
        for elem in lista_barrio:
            try:
                Barrio.create(nombre_barrio=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla barrios. {e}")
        print("Se han persistido los barrios en la BD.")

        lista_licitacion_anio = list(data_frame["licitacion_anio"].unique())
        for elem in lista_licitacion_anio:
            try:
                LicitacionAnio.create(licitacion_anio=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla licitaciones_anio. {e}")
        print("Se han persistido los años de las licitaciones en la BD.")

        data_frame_empresa = data_frame[["empresa","cuit"]]
        data_frame_empresa = data_frame_empresa.drop_duplicates()
        lista_empresa = data_frame_empresa.values

        for elem in lista_empresa:
            try:
                Empresa.create(nombre_empresa=elem[0], cuit=elem[1])
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla empresas. {e}")
        print("Se han persistido las empresas en la BD.")

        for elem in data_frame.values:
            entorno = Entorno.get(Entorno.nombre_entorno == elem[1])
            nombre = elem[2]
            etapa = Etapa.get(Etapa.nombre_etapa==elem[3])
            tipo_obra = Tipo.get(Tipo.nombre_tipo==elem[4])
            area_responsable = AreaResponsable.get(AreaResponsable.area_responsable==elem[5])
            descripcion = elem[6]
            monto_contrato = elem[7]
            comuna = Comuna.get(Comuna.nombre_comuna==elem[8])
            barrio = Barrio.get(Barrio.nombre_barrio==elem[9])
            direccion = elem[10]
            latitud = elem[11]
            longitud = elem[12]
            fecha_inicio = elem[13]
            fecha_fin_inicial = elem[14]
            plazo_meses = elem[15]
            porcentaje_avance = elem[16]
            imagen_1 = elem[17]
            empresa = Empresa.get(Empresa.cuit==elem[20])
            licitacion_anio = LicitacionAnio.get(LicitacionAnio.licitacion_anio==elem[19])
            link_interno = elem[21]
            try:
                Obras.create(entorno=entorno,nombre=nombre, etapa=etapa, tipo_obra=tipo_obra,
                             area_responsable=area_responsable, descripcion=descripcion, monto_contrato=monto_contrato,
                             comuna=comuna, barrio=barrio, direccion=direccion, latitud=latitud, longitud=longitud, fecha_inicio=fecha_inicio, fecha_fin_inicial=fecha_fin_inicial, plazo_meses=plazo_meses, porcentaje_avance=porcentaje_avance, imagen_1=imagen_1, empresa=empresa, licitacion_anio=licitacion_anio, link_interno=link_interno)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla obras. {e}")
        print("Se han persistido las obras en la BD.")
 
    @classmethod
    def nueva_obra():
        pass

    @classmethod
    def obtener_indicadores():
        pass


gestionar_obra = GestionarObra()
# gestionar_obra.conectar_db()
# gestionar_obra.mapear_orm()
data_frame = gestionar_obra.extraer_datos()
df = gestionar_obra.limpiar_datos(data_frame)
# gestionar_obra.cargar_datos(df)