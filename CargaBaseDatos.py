
import psycopg2
  
conn = psycopg2.connect(database="saber11",
                        user='postgres', password='Proyecto2', 
                        host='proyecto2.csd1nefyxik0.us-east-1.rds.amazonaws.com', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
# cursor.execute('DROP TABLE tabla1')

sql ='''CREATE TABLE tabla1(\
    cole_area_ubicacion     varchar NOT NULL,\
    estu_genero             smallint NOT NULL,\
    cole_naturaleza         varchar NOT NULL,\
    fami_estratovivienda    smallint NOT NULL,\
    Personas_hogar          varchar NOT NULL,\
    Educacion_Madre         varchar NOT NULL,\
    Educacion_Padre         varchar NOT NULL,\
    Puntaje_obtenido        varchar NOT NULL\
);'''
  
# sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
# employee_name char(20),\
# employee_email varchar(30), employee_salary float);'''
  
  
cursor.execute(sql)
  
sql = '''copy tabla1(cole_area_ubicacion,estu_genero,cole_naturaleza,fami_estratovivienda,Personas_hogar,Educacion_Madre,Educacion_Padre,Puntaje_obtenido) 
FROM '/home/jpc/Analitica_P_final/datos_filtrados.csv' DELIMITER ',' CSV HEADER;'''

cursor.execute(sql)
  
sql = 'ALTER TABLE tabla1 ADD COLUMN id SERIAL PRIMARY KEY;'

cursor.execute(sql)

sql = '''select * from tabla1 limit 5;'''
cursor.execute(sql)

# for i in cursor.fetchall():
#     print(i)

conn.commit()
conn.close()