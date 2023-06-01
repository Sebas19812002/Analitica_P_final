
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Datos_sin_filtro.csv")
datos.head()
print(datos)


# Conocer los datos que contiene cada Columna
for columna in datos.columns:
    categorias = datos[columna].unique()

    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()

#Eliminar datos 
columnas_a_eliminar = ['periodo']
datos_nuevas_col = datos.drop(columnas_a_eliminar, axis=1)

# Conocer los datos que contiene cada Columna
for columna in datos_nuevas_col.columns:
    categorias = datos_nuevas_col[columna].unique()

    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()


# Eliminar datos incoherentes 
valores_validos = ['F', 'M']
datos_filtrados = datos_nuevas_col[datos_nuevas_col['estu_genero'].isin(valores_validos)]
 
####  'fami_educacionmadre'
valores_validos = ['Secundaria (Bachillerato) completa', 'Primaria incompleta', 'Ninguno',
                   'Postgrado', 'No sabe', 'Primaria completa', 'Técnica o tecnológica completa',
                   'Técnica o tecnológica incompleta', 'Secundaria (Bachillerato) incompleta',
                   'Educación profesional completa','Educación profesional incompleta','No Aplica']

datos_filtrados = datos_nuevas_col[datos_nuevas_col['fami_educacionmadre'].isin(valores_validos)]

####  'fami_educacionpadre'
valores_validos = ['Secundaria (Bachillerato) completa', 'Primaria incompleta', 'Ninguno',
                   'Postgrado', 'No sabe', 'Primaria completa', 'Técnica o tecnológica completa',
                   'Técnica o tecnológica incompleta', 'Secundaria (Bachillerato) incompleta',
                   'Educación profesional completa','Educación profesional incompleta','No Aplica']

datos_filtrados = datos_nuevas_col[datos_nuevas_col['fami_educacionpadre'].isin(valores_validos)]

####  'fami_estratovivienda'
valores_validos = [['Estrato 2','Estrato 1','Sin Estrato', 'Estrato 3', 'Estrato 4' ,'Estrato 6',
                    'Estrato 5','No sabe','Ninguno']]

datos_filtrados = datos_nuevas_col[datos_nuevas_col['fami_educacionpadre'].isin(valores_validos)]

####  'fami_personashogar'
valores_validos = ['3 a 4', '5 a 6', '7 a 8', '1 a 2' ,'9 o más']

datos_filtrados = datos_nuevas_col[datos_nuevas_col['fami_personashogar'].isin(valores_validos)]

for columna in datos_filtrados.columns:
    categorias = datos_filtrados[columna].unique()

    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()

datos_filtrados = datos_filtrados.dropna()

# Datos categorizados 
def categorizar_personas_hogar(fami_personashogar):
    if fami_personashogar == '1 a 2' or fami_personashogar == '3 a 4':
        return 'Poco'
    elif fami_personashogar == '5 a 6':
        return 'Medio'
    else:
        return 'Alto'

datos_filtrados['Personas_hogar'] = datos_filtrados['fami_personashogar'].apply(categorizar_personas_hogar)


def categorizar_educacion_madre(fami_educacionmadre):
    if fami_educacionmadre == 'Secundaria (Bachillerato) completa' :
        return 'SBC'
    elif fami_educacionmadre == 'Primaria incompleta':
        return 'PI'
    elif fami_educacionmadre == 'Ninguno':
        return 'N'
    elif fami_educacionmadre == 'Postgrado':
        return 'P'
    elif fami_educacionmadre == 'No sabe':
        return 'NS'
    elif fami_educacionmadre == 'Primaria completa':
        return 'PC'
    elif fami_educacionmadre == 'Técnica o tecnológica completa':
        return 'TC'
    elif fami_educacionmadre == 'Técnica o tecnológica incompleta':
        return 'TI'
    elif fami_educacionmadre == 'Secundaria (Bachillerato) incompleta':
        return 'SBI'
    elif fami_educacionmadre == 'Educación profesional completa':
        return 'EPC'
    elif fami_educacionmadre == 'Educación profesional incompleta':
        return 'EPI'
    elif fami_educacionmadre == 'No Aplica':
        return 'NA'

    else:
        return 'Hay algo mal'

datos_filtrados['Educacion_Madre'] = datos_filtrados['fami_educacionmadre'].apply(categorizar_educacion_madre)

def categorizar_educacion_padre(fami_educacionpadre):
    if fami_educacionpadre == 'Secundaria (Bachillerato) completa' :
        return 'SBC'
    elif fami_educacionpadre == 'Primaria incompleta':
        return 'PI'
    elif fami_educacionpadre == 'Postgrado':
        return 'P'
    elif fami_educacionpadre == 'No sabe':
        return 'NS'
    elif fami_educacionpadre == 'Ninguno':
        return 'N'
    elif fami_educacionpadre == 'Técnica o tecnológica completa':
        return 'TC'
    elif fami_educacionpadre == 'Primaria completa':
        return 'PC'
    elif fami_educacionpadre == 'Educación profesional completa':
        return 'EPC'
    elif fami_educacionpadre == 'No Aplica':
        return 'NA'
    elif fami_educacionpadre == 'Secundaria (Bachillerato) incompleta':
        return 'SBI'
    elif fami_educacionpadre == 'Educación profesional incompleta':
        return 'EPI'
    elif fami_educacionpadre == 'Técnica o tecnológica incompleta':
        return 'TI'
       
    else:
        return 'Hay algo mal'

datos_filtrados['Educacion_Padre'] = datos_filtrados['fami_educacionpadre'].apply(categorizar_educacion_padre)

def categorizar_puntaje(punt_global):
    if punt_global >= 320 :
        return 'Aceptado'
    elif punt_global < 320:
        return 'Rechazado'
    else:
        return 'Hay algo mal'

datos_filtrados['Puntaje_obtenido'] = datos_filtrados['punt_global'].apply(categorizar_puntaje)


### Eliminar las columnas sin categorizar 
columnas_a_eliminar = ['fami_personashogar','fami_educacionmadre','fami_educacionpadre','punt_global']
datos_filtrados = datos_filtrados.drop(columnas_a_eliminar, axis=1)





for columna in datos_filtrados.columns:
    categorias = datos_filtrados[columna].unique()

    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()


