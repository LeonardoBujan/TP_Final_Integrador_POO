from abc import ABC
from peewee import *
import pandas as pd
import os
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
                        LicitacionAnio, ContratacionTipo, Empresa, Obras])
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

        lista_contratacion_tipo = list(data_frame["contratacion_tipo"].unique())
        for elem in lista_contratacion_tipo:
            try:
                ContratacionTipo.create(contratacion_tipo=elem)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla contrataciones_tipo. {e}")        
        print("Se han persistido los tipos de contrataciones en la BD.")

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
            empresa = Empresa.get(Empresa.cuit==elem[22])
            licitacion_anio = LicitacionAnio.get(LicitacionAnio.licitacion_anio==elem[19])
            contratacion_tipo = ContratacionTipo.get(ContratacionTipo.contratacion_tipo==elem[20])
            nro_contratacion = elem[21]
            mano_obra = elem[23]
            destacada = elem[24]
            link_interno = elem[25]
            expediente_numero = elem[26]
            financiamiento = elem[27]
            try:
                Obras.create(entorno=entorno,nombre=nombre, etapa=etapa, tipo_obra=tipo_obra,
                             area_responsable=area_responsable, descripcion=descripcion, monto_contrato=monto_contrato,
                             comuna=comuna, barrio=barrio, direccion=direccion, latitud=latitud, longitud=longitud, fecha_inicio=fecha_inicio, fecha_fin_inicial=fecha_fin_inicial, plazo_meses=plazo_meses, porcentaje_avance=porcentaje_avance, imagen_1=imagen_1, empresa=empresa, licitacion_anio=licitacion_anio, contratacion_tipo=contratacion_tipo, nro_contratacion=nro_contratacion, mano_obra=mano_obra, destacada=destacada, expediente_numero=expediente_numero, financiamiento=financiamiento, link_interno=link_interno)
            except IntegrityError as e:
                print(f"Error al insertar un nuevo registro en la tabla obras. {e}")
        print("Se han persistido las obras en la BD.")
 
    @classmethod
    def nueva_obra(cls):
        existe_base_datos = os.path.exists(f"{obtener_directorio()}/obras_urbanas.db")
        if existe_base_datos:
            cls.conectar_db()
        else:
            data_frame = cls.extraer_datos()
            cls.conectar_db()
            cls.mapear_orm()        
            cls.cargar_datos(cls.limpiar_datos(data_frame))
        
        obra_1 = Obras()
        nuevo_proyecto = obra_1.nuevo_proyecto()
        licitacion = obra_1.iniciar_contratación()
        adjudicar = obra_1.adjudicar_obra()
        iniciar = obra_1.iniciar_obra()
        avanace = obra_1.actualizar_porcentaje_avace()

        try:
            Obras.create(entorno=nuevo_proyecto[0],
                         nombre=nuevo_proyecto[1], 
                         etapa=nuevo_proyecto[2], 
                         tipo_obra=nuevo_proyecto[3],
                         area_responsable=nuevo_proyecto[4], 
                         descripcion=nuevo_proyecto[5], 
                         monto_contrato=nuevo_proyecto[6],
                         comuna=nuevo_proyecto[7], 
                         barrio=nuevo_proyecto[8], 
                         direccion=nuevo_proyecto[9], 
                         latitud=nuevo_proyecto[10], 
                         longitud=nuevo_proyecto[11], 
                         fecha_inicio=iniciar[1], 
                         fecha_fin_inicial=iniciar[2],
                         plazo_meses=nuevo_proyecto[12], 
                         porcentaje_avance=avanace, 
                         imagen_1=nuevo_proyecto[13], 
                         empresa=adjudicar[0], 
                         licitacion_anio=nuevo_proyecto[14], 
                         contratacion_tipo=licitacion[0], 
                         nro_contratacion=licitacion[1],
                         mano_obra=iniciar[4], 
                         destacada=iniciar[0], 
                         expediente_numero=adjudicar[1], 
                         financiamiento=iniciar[3], 
                         link_interno=nuevo_proyecto[15])
            print("Se ha ingresado una nueva Obra en la BD.")
        except IntegrityError as e:
            print(f"Error al insertar un nuevo registro en la tabla obras. {e}")       

        obra_2 = Obras()
        nuevo_proyecto = obra_2.nuevo_proyecto()
        licitacion = obra_2.iniciar_contratación()
        adjudicar = obra_2.adjudicar_obra()
        iniciar = obra_2.iniciar_obra()
        avanace = obra_2.actualizar_porcentaje_avace()

        try:
            Obras.create(entorno=nuevo_proyecto[0],
                         nombre=nuevo_proyecto[1], 
                         etapa=nuevo_proyecto[2], 
                         tipo_obra=nuevo_proyecto[3],
                         area_responsable=nuevo_proyecto[4], 
                         descripcion=nuevo_proyecto[5], 
                         monto_contrato=nuevo_proyecto[6],
                         comuna=nuevo_proyecto[7], 
                         barrio=nuevo_proyecto[8], 
                         direccion=nuevo_proyecto[9], 
                         latitud=nuevo_proyecto[10], 
                         longitud=nuevo_proyecto[11], 
                         fecha_inicio=iniciar[1], 
                         fecha_fin_inicial=iniciar[2],
                         plazo_meses=nuevo_proyecto[12], 
                         porcentaje_avance=avanace, 
                         imagen_1=nuevo_proyecto[13], 
                         empresa=adjudicar[0], 
                         licitacion_anio=nuevo_proyecto[14], 
                         contratacion_tipo=licitacion[0], 
                         nro_contratacion=licitacion[1],
                         mano_obra=iniciar[4], 
                         destacada=iniciar[0], 
                         expediente_numero=adjudicar[1], 
                         financiamiento=iniciar[3], 
                         link_interno=nuevo_proyecto[15])
            print("Se ha ingresado una nueva Obra en la BD.")
        except IntegrityError as e:
            print(f"Error al insertar un nuevo registro en la tabla obras. {e}")

        obra_1.finalizar_obra()
        obra_2.rescindir_obra()

    @classmethod
    def obtener_indicadores(cls):
        # Listado de todas las áreas responsables.
        print("\nLISTADO DE LAS AREAS RESPONSABLES")
        for area_responsable in AreaResponsable.select():
            print(f"{area_responsable.id} - {area_responsable.area_responsable}")

        # Listado de todos los tipos de obra. 
        print("\nLISTADO DE TODOS LOS TIPO DE OBRAS")
        for tipo_obra in Tipo.select():
            print(f"{tipo_obra.id} - {tipo_obra.nombre_tipo}")

        # Cantidad de obras que se encuentran en cada etapa.
        print("\nCANTIDAD DE OBRAS QUE SE ENCUENTRAN EN CADA ETAPA")
        obras_etapas = Etapa.select(Etapa, fn.Count(Obras.etapa_id).alias("cantidad")).join(Obras).group_by(Etapa)
        for resultado in obras_etapas:
            print(f"Etapa {resultado.nombre_etapa} - cantidad {resultado.cantidad}")

        # Cantidad de obras por tipo de obra. 
        print("\nCANTIDAD DE OBRAS POR TIPO DE OBRA")
        obras_tipo = Tipo.select(Tipo, fn.Count(Obras.tipo_obra_id).alias("cantidad")).join(Obras).group_by(Tipo)
        for resultado in obras_tipo:
            print(f"Tipo de obra {resultado.nombre_tipo} - cantidad {resultado.cantidad}")

        # Listado de todos los barrios pertenecientes a las comunas 1, 2 y 3.
        print("\nLISTADO DE LOS BARRIOS QUE PERTENECEN A LA COMUNA 1, 2 Y 3")
        barrios_comuna = Barrio.select(Barrio).join(Obras).distinct().where(Obras.comuna_id.in_([1,2,3]))
        for resultado in barrios_comuna:
            print(f"Barrio nombre {resultado.nombre_barrio}")

        # Cantidad de obras “Finalizadas” en la comuna 1. 
        print("\nCANTIDAD DE OBRAS FINALIZADAS EN LA COMUNA 1")
        comuna_obra_finalizada = Comuna.select(fn.Count(Obras.comuna_id).alias("cantidad")).join(Obras).where((Comuna.nombre_comuna == 1) & (Obras.etapa_id == 1))
        for resultado in comuna_obra_finalizada:
            print(f"Obras finalizadas {resultado.cantidad}")

        # Cantidad de obras “Finalizadas” en un plazo menor o igual a 24 meses. 
        print("\nCANTIDAD DE OBRAS FINALIZADAS EN UN PLAZO MENOR A 24 MESES")
        obra_finalizada_plazo = Obras.select(fn.Count(Obras.id).alias("cantidad")).where(Obras.plazo_meses <= 24)
        for resultado in obra_finalizada_plazo:
            print(f"Obras finalizadas {resultado.cantidad}")


def main() -> None:
    GestionarObra().nueva_obra()
    GestionarObra().obtener_indicadores()

if __name__ == '__main__':
    main()