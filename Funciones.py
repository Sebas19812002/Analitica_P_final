#Creación de las visualizaciones

"1. Exploración de los datos--------------------------------------------------------------"
#Graficos de pie
def Conexion_DB_():
    import pandas as pd
    import psycopg2
    import os
    from dotenv import load_dotenv
    # path to env file
    env_path='Informacion.env'
    # load env 
    load_dotenv(dotenv_path=env_path)
    # extract env variables
    DBUSER=os.getenv('DBUSER')
    DBPASSWORD=os.getenv('DBPASSWORD')
    DBHOST=os.getenv('DBHOST')
    DBPORT=os.getenv('DBPORT')
    DBNAME=os.getenv('DBNAME')
    #connect to DB
    engine = psycopg2.connect(
        dbname=DBNAME,
        user=DBUSER,
        password=DBPASSWORD,
        host=DBHOST,
        port=DBPORT
    )
    
    cursor = engine.cursor()
    
    query = "SELECT * FROM tabla1;"
    
    cursor.execute(query)
    data=cursor.fetchall()
    df=pd.DataFrame(data,columns=['cole_area_ubicacion',
                                  'estu_genero',
                                  'cole_naturaleza',
                                  'fami_estratovivienda',
                                  'Personas_hogar',
                                  'Educacion_Madre',
                                  'Educacion_Padre',
                                  'Puntaje_obtenido',
                                  'id'])
    datos=df.drop("id", axis=1)
    return datos


def estimar(radio1,radio2,radio3,radio4, dropdown1, dropdown2, dropdown3, dropdown4):
    from pgmpy.inference import VariableElimination
    from pgmpy.readwrite import BIFReader
    Sex=9
    if radio1 == 'Femenino':
       Sex="1"
    elif radio1 ==  'Masculino':
       Sex="0"
   
    Ubicacion=9
    if radio2 == 'Urbano':
       Ubicacion="URBANO"
    elif radio2 ==  'Rural':
       Ubicacion="RURAL"
     
    Colegio=9
    if radio3 == 'Oficial':
       Colegio="Oficial"
    elif radio3 ==  'No Oficial':
       Colegio="No_oficial"   
    
    Estrato = 9
    if dropdown1 == "Estrato 1":
        Estrato = "1"
    elif dropdown1 == "Estrato 2":
        Estrato= "2"
    elif dropdown1 == "Estrato 3":
        Estrato = "3"
    elif dropdown1 == "Estrato 4":
        Estrato ="4"
    elif dropdown1 == "Estrato 5":
        Estrato ="5"   
    elif dropdown1 == "Estrato 6":
        Estrato ="6"
    elif dropdown1 == "Sin Estrato":
        Estrato ="0"
    
    Per_Hogar = 9
    if dropdown2 == "1 a 4":
        Per_Hogar = "Poco"
    elif dropdown2 == "5 a 6":
        Per_Hogar= "Medio"
    elif dropdown2 == "Más de 7":
        Per_Hogar = "Alto"
       
        
    Edu_madre = 9
    if dropdown3 == 'Secundaria (Bachillerato) completa' :
        Edu_madre = 'SBC'
    elif dropdown3 == 'Primaria incompleta':
        Edu_madre = 'PI'
    elif dropdown3 == 'Ninguno':
        Edu_madre = 'N'
    elif dropdown3 == 'Postgrado':
        Edu_madre = 'P'
    elif dropdown3 == 'No sabe':
        Edu_madre = 'NS'
    elif dropdown3 == 'Primaria completa':
        Edu_madre = 'PC'
    elif dropdown3 == 'Técnica o tecnológica completa':
        Edu_madre = 'TC'
    elif dropdown3 == 'Técnica o tecnológica incompleta':
        Edu_madre = 'TI'
    elif dropdown3 == 'Secundaria (Bachillerato) incompleta':
        Edu_madre = 'SBI'
    elif dropdown3 == 'Educación profesional completa':
        Edu_madre = 'EPC'
    elif dropdown3 == 'Educación profesional incompleta':
        Edu_madre = 'EPI'
    elif dropdown3 == 'No Aplica':
        Edu_madre = 'NAP'



    Edu_padre = 9
    if dropdown4 == 'Secundaria (Bachillerato) completa' :
        Edu_padre = 'SBC'
    elif dropdown4 == 'Primaria incompleta':
        Edu_padre = 'PI'
    elif dropdown4 == 'Ninguno':
        Edu_padre = 'N'
    elif dropdown4 == 'Postgrado':
        Edu_padre = 'P'
    elif dropdown4 == 'No sabe':
        Edu_padre = 'NS'
    elif dropdown4 == 'Primaria completa':
        Edu_padre = 'PC'
    elif dropdown4 == 'Técnica o tecnológica completa':
        Edu_padre = 'TC'
    elif dropdown4 == 'Técnica o tecnológica incompleta':
        Edu_padre = 'TI'
    elif dropdown4 == 'Secundaria (Bachillerato) incompleta':
        Edu_padre = 'SBI'
    elif dropdown4 == 'Educación profesional completa':
        Edu_padre = 'EPC'
    elif dropdown4 == 'Educación profesional incompleta':
        Edu_padre = 'EPI'
    elif dropdown4 == 'No Aplica':
        Edu_padre = 'NAP'
        
    if radio4=="Modelo Normal":
        modelo = BIFReader("Modelo.bif").get_model()
    else:   
        modelo = BIFReader("Modelo_suavizado.bif").get_model()
    
    inferencia = VariableElimination(modelo)
    evidencia = {}
    
    if Sex !=9: 
        evidencia["estu_genero"]= Sex
    if Ubicacion !=9: 
        evidencia["cole_area_ubicacion"]= Ubicacion
    if Colegio !=9: 
        evidencia["cole_naturaleza"]= Colegio
    if Estrato !=9: 
        evidencia["fami_estratovivienda"]= Estrato
    if Per_Hogar !=9: 
        evidencia["Personas_hogar"]= Per_Hogar
    if Edu_madre !=9: 
        evidencia["Educacion_Madre"]= Edu_madre
    if Edu_padre !=9: 
        evidencia["Educacion_Padre"]= Edu_padre

    resultado = inferencia.query(['Puntaje_obtenido'],evidence=evidencia).values
    return resultado


