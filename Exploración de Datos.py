
import pandas as pd


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
def categorizar_genero(estu_genero):
    if estu_genero == 'F' :
        return 1
    else:
        return 0
datos_filtrados['estu_genero'] = datos_filtrados['estu_genero'].apply(categorizar_genero) 
    
def categorizar_personas_hogar(fami_personashogar):
    if fami_personashogar == '1 a 2' or fami_personashogar == '3 a 4':
        return 'Poco'
    elif fami_personashogar == '5 a 6':
        return 'Medio'
    else:
        return 'Alto'
def categorizar_estrato(fami_estratovivienda):
    if fami_estratovivienda == 'Estrato 1':
        return 1
    elif fami_estratovivienda == 'Estrato 2':
        return 2
    elif fami_estratovivienda == 'Estrato 3':
        return 3
    elif fami_estratovivienda == 'Estrato 4':
        return 4
    elif fami_estratovivienda == 'Estrato 5':
        return 5
    elif fami_estratovivienda == 'Estrato 6':
        return 6
    else:
        return 0
def categorizar_cole(cole_naturaleza):
    if cole_naturaleza == 'OFICIAL':
        return "Oficial"
    else:
        return "No_oficial"
datos_filtrados['cole_naturaleza'] = datos_filtrados['cole_naturaleza'].apply(categorizar_cole)
        
datos_filtrados['fami_estratovivienda'] = datos_filtrados['fami_estratovivienda'].apply(categorizar_estrato)

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
        return 'NAP'

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
        return 'NAP'
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
    if punt_global >= 300 :
        return 'Aceptado'
    elif punt_global < 300:
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
print(datos_filtrados.dtypes)

Aceptados = datos_filtrados['Puntaje_obtenido'].value_counts()['Aceptado']
Rechazados = datos_filtrados['Puntaje_obtenido'].value_counts()['Rechazado']



#Equilibrar muestra
condicion = datos_filtrados['Puntaje_obtenido'] == 'Rechazado'
indices_a_eliminar = datos_filtrados[condicion].sample(n=60000).index
df_sin_filas = datos_filtrados.drop(indices_a_eliminar)

of= df_sin_filas['cole_naturaleza'].value_counts()['Oficial']
noof = df_sin_filas['cole_naturaleza'].value_counts()['No_oficial']

Aceptados = df_sin_filas['Puntaje_obtenido'].value_counts()['Aceptado']
Rechazados= df_sin_filas['Puntaje_obtenido'].value_counts()['Rechazado']

#datos_filtrados.to_csv("datos_filtrados", index=False)
