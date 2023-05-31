
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("Datos_filtrados.csv")
datos.head()

#Visualizaciones de los datos:
"1. Exploración de los datos"
#Graficos de pie
#Género

fig, ax = plt.subplots()
etiquetas = ["Mujeres","Hombres"]
valores = [datos.loc[(datos['estu_genero'] == "F")].shape[0],(datos["estu_genero"]=="M").sum()]
colores=["#D7F47C", "#81E2DF"]
ax.pie(valores, labels = etiquetas ,colors=colores, autopct='%1.1f%%')
plt.title("Sexo de la muestra", fontsize = 18)
plt.show() 
