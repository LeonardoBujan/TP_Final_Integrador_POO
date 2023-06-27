from peewee import *
from directorio import *

sqlite_db = SqliteDatabase(f"{obtener_directorio()}/obras_urbanas.db", pragmas={'journal_mode': 'wal'})

class BaseModel(Model):    

    class Meta:
        database = sqlite_db

class Entorno(BaseModel):
    nombre_entorno = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre_entorno

    class Meta:
        db_table = "entornos"


class Etapa(BaseModel):
    nombre_etapa = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre_etapa

    class Meta:
        db_table = "etapas"


class Tipo(BaseModel):
    nombre_tipo = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre_tipo

    class Meta:
        db_table = "tipos_obra"


class AreaResponsable(BaseModel):
    area_responsable = CharField(unique=True)

    def __str__(self) -> str:
        return self.area_responsable

    class Meta:
        db_table = "areas_responsable"

class Comuna(BaseModel):
    nombre_comuna = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre_comuna
    
    class Meta:
        db_table = "comunas"

class Barrio(BaseModel):
    nombre_barrio = CharField(unique=True)

    def __str__(self) -> str:
        return self.nombre_barrio

    class Meta:
        db_table = "barrios"


class LicitacionAnio(BaseModel):
    licitacion_anio = IntegerField(unique=True)

    def __str__(self) -> str:
        return self.licitacion_anio

    class Meta:
        db_table = "licitaciones_anio"


class ContratacionTipo(BaseModel):
    contratacion_tipo = CharField(unique=True)

    def __str__(self) -> str:
        return self.contratacion_tipo
    
    class Meta:
        db_table = "contrataciones_tipo"

class Empresa(BaseModel):
    nombre_empresa = CharField()
    cuit = CharField()

    def __str__(self) -> str:
        return f"Empresa: {self.nombre_empresa} , CUIT: {self.cuit}"

    class Meta:
        db_table = "empresas"


class Obras(BaseModel):
  
    entorno = ForeignKeyField(Entorno, backref="entornos")
    nombre = CharField()
    etapa = ForeignKeyField(Etapa, backref="etapas")
    tipo_obra = ForeignKeyField(Tipo, backref="tipos_obra")
    area_responsable = ForeignKeyField(AreaResponsable, backref="areas_responsable")
    descripcion = TextField()
    monto_contrato = IntegerField()
    comuna = ForeignKeyField(Comuna, backref="comunas")
    barrio = ForeignKeyField(Barrio, backref="barrios")
    direccion = TextField()
    latitud = CharField()
    longitud = CharField()
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = IntegerField()
    porcentaje_avance = IntegerField()
    imagen_1 = TextField()
    empresa = ForeignKeyField(Empresa, backref="empresas")
    licitacion_anio = ForeignKeyField(LicitacionAnio, backref="licitaciones_anio")
    contratacion_tipo = ForeignKeyField(ContratacionTipo, backref="contrataciones_tipo")
    nro_contratacion = CharField()
    mano_obra = IntegerField()
    destacada = CharField()
    link_interno = CharField()
    expediente_numero = CharField()
    financiamiento = CharField()
    
    class Meta:
        db_table = "obras"

    def nuevo_proyecto(self):
        print("\nA continuación deberá ingresar los datos del proyecto nuevo")

        print("Seleccione el entorno al que pertenece el nuevo proyecto")        
        validacion_numero = []
        for entorno in Entorno.select():
            print(f"{entorno.id} - {entorno.nombre_entorno}")
            validacion_numero.append(entorno.id)
        while True:
            try:                
                entorno_proyecto_nuevo = int(input("Seleccione el número correspondiente al entorno del proyecto\n--> "))
                while True:
                    try:
                        validacion_numero.index(entorno_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    entorno_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        nombre_proyecto_nuevo = input("Escriba el nombre para el proyecto\n--> ")
        while nombre_proyecto_nuevo == "":
            nombre_proyecto_nuevo = input("Escriba el nombre para el proyecto\n--> ")

        etapa_proyecto_nuevo = ""
        for etapas in Etapa.select():
            if etapas.nombre_etapa == "Proyecto":
                etapa_proyecto_nuevo = etapas.id
                # print("La etapa Proyecto ya se encuentra en la BD.")
                break
        if etapa_proyecto_nuevo == "":
            try:
                Etapa(nombre_etapa = "Proyecto").save()
                etapa_proyecto_nuevo = Etapa.get(Etapa.nombre_etapa == "Proyecto")
                # print(f"Se guardo la etapa Proyecto en la BD.")
            except IntegrityError as e:
                print("Error al insertar en la tabla categories.", e)

        print("Seleccione el número del tipo de obra para el nuevo proyecto")
        validacion_numero_obra = []
        for tipos_obra in Tipo.select():
            print(f"{tipos_obra.id} - {tipos_obra.nombre_tipo}")
            validacion_numero_obra.append(tipos_obra.id)     
        
        while True:
            try:                
                tipo_obra_proyecto_nuevo = int(input("Seleccione el número correspondiente al tipo de obra\n--> "))
                while True:
                    try:
                        validacion_numero_obra.index(tipo_obra_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    tipo_obra_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")


        print("\nSeleccione el area responsable para el nuevo proyecto")
        validacion_numero_area = []
        for area_responsable in AreaResponsable.select():
            print(f"{area_responsable.id} - {area_responsable.area_responsable}")
            validacion_numero_area.append(area_responsable.id)

        while True:
            try:                
                area_responsable_nuevo = int(input("Seleccione el número correspondiente al area reponsable del proyecto\n--> "))
                while True:
                    try:
                        validacion_numero_area.index(area_responsable_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    area_responsable_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        descripcion_proyecto_nuevo = input("Escriba una descripción del proyecto\n--> ")

        while True:
            try:
                monto_contrato_proyecto_nuevo = int(input("Escriba el monto de contrato total de obra del proyecto\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado debe ser numérico")

        print("\nSeleccione la comuna correspondiente al nuevo proyecto")
        validacion_numero_comuna = []
        for comuna in Comuna.select():
            print(f"{comuna.id} - Comuna {comuna.nombre_comuna}")
            validacion_numero_comuna.append(comuna.id)        

        while True:
            try:                
                comuna_proyecto_nuevo = int(input("Seleccione el número correspondiente a la comuna del nuevo proyecto\n--> "))
                while True:
                    try:
                        validacion_numero_comuna.index(comuna_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    comuna_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        print("\nSeleccione el barrio correspondiente al nuevo proyecto")
        validacion_numero_barrio = []
        for barrio in Barrio.select():
            print(f"{barrio.id} - {barrio.nombre_barrio}")
            validacion_numero_barrio.append(barrio.id)        

        while True:
            try:                
                barrio_proyecto_nuevo = int(input("Seleccione el número correspondiente al barrio del nuevo proyecto\n--> "))
                while True:
                    try:
                        validacion_numero_barrio.index(barrio_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    barrio_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        direccion_proyecto_nuevo = input("Escriba la dirección del proyecto nuevo\n--> ")
        while direccion_proyecto_nuevo == "":
            direccion_proyecto_nuevo = input("Escriba la dirección del proyecto nuevo\n--> ")

        latitud_proyecto_nuevo = input("Escriba la coordenada de latitud de dirección del proyecto nuevo\n--> ")

        longitud_proyecto_nuevo = input("Escriba la coordenada de longitud de dirección del proyecto nuevo\n--> ")

        while True:
            try:
                plazo_meses_proyecto_nuevo = int(input("Escriba el plazo en meses para el proyecto nuevo\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado debe ser numérico")

        imagen_1_proyecto_nuevo = input("Escriba la url de la imagen del proyecto nuevo\n--> ")

        anio = int(input("Escriba el año de licitacion del proyecto\n--> "))
        licitacion_anio_proyecto_nuevo = ""

        for elem in LicitacionAnio.select():
            if elem.licitacion_anio == anio:
                licitacion_anio_proyecto_nuevo = elem.id
                break

        if licitacion_anio_proyecto_nuevo == "":
            try:
                LicitacionAnio(licitacion_anio = anio).save()
                licitacion_anio_proyecto_nuevo = LicitacionAnio.get(LicitacionAnio.licitacion_anio == anio)
            except IntegrityError as e:
                print("Error al insertar en la tabla categories.", e)

        link_interno_proyecto_nuevo = input("Escriba la url del link interno correspondiente al proyecto nuevo\n--> ")

        return [entorno_proyecto_nuevo,
                nombre_proyecto_nuevo, 
                etapa_proyecto_nuevo, 
                tipo_obra_proyecto_nuevo, 
                area_responsable_nuevo, 
                descripcion_proyecto_nuevo,
                monto_contrato_proyecto_nuevo,
                comuna_proyecto_nuevo, 
                barrio_proyecto_nuevo, 
                direccion_proyecto_nuevo,
                latitud_proyecto_nuevo, 
                longitud_proyecto_nuevo, 
                plazo_meses_proyecto_nuevo, 
                imagen_1_proyecto_nuevo, 
                licitacion_anio_proyecto_nuevo, 
                link_interno_proyecto_nuevo]


    def iniciar_contratación(self):
        print("\nA continuación seleccione el tipo de contratación y escriba el nro de contrato del proyecto")
        validacion_numero_contratacion = []
        for contratacion in ContratacionTipo.select():
            print(f"{contratacion.id} - {contratacion.contratacion_tipo}")
            validacion_numero_contratacion.append(contratacion.id)        
        
        while True:
            try:                
                tipo_contratacion_proyecto_nuevo = int(input("Seleccione el número correspondiente al entorno del proyecto\n--> "))
                while True:
                    try:
                        validacion_numero_contratacion.index(tipo_contratacion_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    tipo_contratacion_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        nro_contrato_proyecto_nuevo = input("Escriba el número de contrato del proyecto\n--> ")

        return [tipo_contratacion_proyecto_nuevo, nro_contrato_proyecto_nuevo]

    def adjudicar_obra(self):
        print("\nA continuación seleccione el nombre de la empresa y escriba el nro de expediente")
        validacion_numero_empresa = []
        for empresa in Empresa.select():
            print(f"{empresa.id} - {empresa.nombre_empresa}")
            validacion_numero_empresa.append(empresa.id)        

        while True:
            try:                
                empresa_proyecto_nuevo = int(input("Seleccione el número correspondiente a la empresa encargada del proyecto\n--> "))
                while True:
                    try:
                        validacion_numero_empresa.index(empresa_proyecto_nuevo)
                        break
                    except ValueError as e:
                        print("El valor ingresado no corresponde a uno de la lista")
                    empresa_proyecto_nuevo = int(input("Seleccione el número dentro de la lista\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado no es numérico. Por favor, ingrese un número")

        nro_expediente_proyecto_nuevo = input("Escriba el número de expediente del proyecto\n--> ")

        return [empresa_proyecto_nuevo, nro_expediente_proyecto_nuevo]

    def iniciar_obra(self):
        destacada = input("Escriba el valor correspondiente en cuanto a si el proyecto es detacado o no\nSI\nNO\n--> ")
        fecha_inicio = input("Escriba la fecha de inicio del proyecto con el formato dd/mm/aaaa\n--> ")
        fecha_fin_inicial = input("Escriba la fecha de fin inicial del proyecto con el formato dd/mm/aaaa\n--> ")
        fuente_financiamiento = input("Escriba la fuente de financiamiento para el proyecto\n--> ")

        while True:
            try:
                mano_obra = int(input("Escriba el valor de la mano de obra del proyecto\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado debe ser numérico")
        
        return [destacada, fecha_inicio, fecha_fin_inicial, fuente_financiamiento, mano_obra]

    def actualizar_porcentaje_avace(self):
        while True:
            try:
                porcentaje_avance = int(input("Escriba el porcentaje de avance de la obra\n--> "))
                break
            except ValueError as e:
                print("El valor ingresado debe ser numérico")

        return porcentaje_avance

    def incrementar_plazo():
        pass
    
    def incrementar_mano_obra():
        pass

    def finalizar_obra(self):
        print("\nLISTA DE OBRAS QUE NO HAN TERMINADO Y SE PUEDEN FINALIZAR")
        obras_sin_terminar = Obras.select().where(Obras.porcentaje_avance < 100)
        for obras in obras_sin_terminar:
            print(f"{obras.id} - {obras.nombre}")
        obra = int(input("Escriba la opción que corresponde al número de obra que desea finalizar\n--> "))
        query = Obras.update(etapa_id = 1, porcentaje_avance = 100).where(Obras.id == obra)
        actualizar = query.execute()
        if actualizar == 1:
            print("La obra ha finalizado.")
        else:
            print("No se guardaron los cambios en la BD.")

    def rescindir_obra(self):
        print("\nLISTA DE OBRAS QUE NO HAN TERMINADO Y SE PUEDEN RESCINDIR")
        obras_a_rescindir = Obras.select().where(Obras.porcentaje_avance < 100)
        for obras in obras_a_rescindir:
            print(f"{obras.id} - {obras.nombre}")
        obra = int(input("Escriba la opción que corresponde al número de obra que desea rescindir\n--> "))

        etapa = 0    
        for etapas in Etapa.select():
            if etapas.nombre_etapa == "Rescindida":
                etapa = etapas.id
                break

        if etapa == 0:
            try:
                Etapa(nombre_etapa = "Rescindida").save()
                etapa = Etapa.get(Etapa.nombre_etapa == "Rescindida")
            except IntegrityError as e:
                print("Error al insertar en la tabla categories.", e)

        query = Obras.update(etapa_id = etapa).where(Obras.id == obra)
        actualizar = query.execute()
        if actualizar == 1:
            print("La obra se ha rescindido.")
        else:
            print("No se guardaron los cambios en la BD.")