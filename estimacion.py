from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import BayesianEstimator
from sklearn.model_selection import train_test_split
from pgmpy.readwrite import BIFReader
from pgmpy.readwrite import BIFWriter
import pandas as pd

df= pd.read_csv("datos_filtrados.csv")
print(df.head(5))
for columna in df.columns:
    categorias = df[columna].unique()
    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()

#Parametrización del modelo
mod_fit = BayesianNetwork([("Educacion_Madre","Personas_hogar"),
                                ("Educacion_Padre","Personas_hogar"),
                                ("Personas_hogar","fami_estratovivienda"),
                                ("fami_estratovivienda","cole_naturaleza"),
                                ("cole_area_ubicacion","cole_naturaleza"),
                                ("cole_naturaleza","Puntaje_obtenido"),
                                ("estu_genero","Puntaje_obtenido"),
                                ("Educacion_Madre","Puntaje_obtenido"),
                                ("Educacion_Padre","Puntaje_obtenido"),
                                ("fami_estratovivienda","Puntaje_obtenido")])


#Depende del test_size, los datos retantes iran a la estimación del modelo

train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

#train_data.to_csv("Datos_entrenamiento",index=False )
#test_data.to_csv("Datos_test", index=False)
train_data=pd.read_csv("Datos_entrenamiento.csv")
mod_fit.fit(data=train_data , estimator = BayesianEstimator)

mod_fit.check_model()


#Serializar el modelo
#writer = BIFWriter(mod_fit)
#writer.write_bif(filename='Modelo.bif')
modelo = BIFReader("Modelo.bif").get_model()

modelo.check_model()

#Ejemplo de inferencia

inferencia = VariableElimination(modelo)
modelo.nodes
Ejemplo1 = inferencia.query(['Puntaje_obtenido'],evidence={"Educacion_Madre":"P","cole_naturaleza":"No_oficial", "Personas_hogar":"Alto", "fami_estratovivienda": "2" })
print("")
print ("Ejemplo 1", Ejemplo1)



