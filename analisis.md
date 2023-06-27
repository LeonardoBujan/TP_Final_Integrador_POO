### Análisis para el proyecto

## Información del Data Set 

RangeIndex: 1409 entries, 0 to 1408
Data columns (total 36 columns):
#   Column                      Non-Null Count  Dtype
---  ------                      --------------  -----
0   ID                          1409 non-null   int64
1   entorno                     1409 non-null   object
2   nombre                      1409 non-null   object
3   etapa                       1409 non-null   object
4   tipo                        1381 non-null   object
5   area_responsable            1409 non-null   object
6   descripcion                 1327 non-null   object
7   monto_contrato              1220 non-null   object
8   comuna                      1401 non-null   object
9   barrio                      1403 non-null   object
10  direccion                   1272 non-null   object
11  lat                         1341 non-null   object
12  lng                         1341 non-null   object
13  fecha_inicio                1325 non-null   object
14  fecha_fin_inicial           1341 non-null   object
15  plazo_meses                 1261 non-null   object
16  porcentaje_avance           1374 non-null   object
17  imagen_1                    982 non-null    object
18  imagen_2                    589 non-null    object
19  imagen_3                    389 non-null    object
20  imagen_4                    240 non-null    object
21  licitacion_oferta_empresa   1215 non-null   object
22  licitacion_anio             940 non-null    object
23  contratacion_tipo           614 non-null    object
24  nro_contratacion            530 non-null    object
25  cuit_contratista            1059 non-null   object
26  beneficiarios               477 non-null    object
27  mano_obra                   275 non-null    object
28  compromiso                  266 non-null    object
29  destacada                   31 non-null     object
30  ba_elige                    7 non-null      object
31  link_interno                990 non-null    object
32  pliego_descarga             561 non-null    object
33  expediente-numero           197 non-null    object
34  estudio_ambiental_descarga  19 non-null     object
35  financiamiento              13 non-null     object

## Columnas involucradas en la exploracion de datos

#   Column                      Non-Null Count  Dtype
---  ------                      --------------  -----
1   entorno                     1409 non-null   object
2   nombre                      1409 non-null   object
3   etapa                       1409 non-null   object
4   tipo                        1381 non-null   object
5   area_responsable            1409 non-null   object
6   descripcion                 1327 non-null   object
7   monto_contrato              1220 non-null   object
8   comuna                      1401 non-null   object
9   barrio                      1403 non-null   object
10  direccion                   1272 non-null   object
11  latitud                     1341 non-null   object
12  longitud                    1341 non-null   object
13  fecha_inicio                1325 non-null   object
14  fecha_fin_inicial           1341 non-null   object
15  plazo_meses                 1261 non-null   object
16  porcentaje_avance           1374 non-null   object
17  imagen_1                    982 non-null    object
21  licitacion_oferta_empresa   1215 non-null   object
22  licitacion_anio             940 non-null    object
23  contratacion_tipo           614 non-null    object
24  nro_contratacion            530 non-null    object
25  cuit_contratista            1059 non-null   object
27  mano_obra                   275 non-null    object
29  destacada                   31 non-null     object
31  link_interno                990 non-null    object
33  expediente-numero           197 non-null    object
35  financiamiento              13 non-null     object

## Columnas que van a ser renombradas en el Data Set

#   Nombre Data Set                 Nombre Actual
    ---------------                 -------------
    lat                             latitud
    lng                             longitud
    licitacion_oferta_empresa       empresa
    cuit_contratista                cuit
    expediente-numero               expediente_numero

## Tablas que se van a crear en la BD

*entorno*
*etapa*
*tipo*
*area_responsable*
*comuna*
*barrio*
*licitacion_anio*
*contrataciones_tipo*
*empresa (licitacion_oferta_empresa cuit_contratista)*
*obras*