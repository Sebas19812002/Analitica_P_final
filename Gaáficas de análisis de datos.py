
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = pd.read_csv("datos_filtrados.csv")
datos.head()

for columna in datos.columns:
    categorias = datos[columna].unique()

    print(f"Categorías de la columna '{columna}':")
    print(categorias)
    print()

#Visualizaciones de los datos:
"1. Exploración de los datos"

# Puntaje y Género
# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

Mujeres_Aprobaron= datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['estu_genero'] == 1)].shape[0]
Mujeres_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['estu_genero'] == 1)].shape[0]
Hombres_Aprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['estu_genero'] == 0)].shape[0]
Hombres_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['estu_genero'] == 0)].shape[0]

y = [ Mujeres_Reprobaron, Hombres_Reprobaron,Mujeres_Aprobaron,Hombres_Aprobaron]
x = ['1','2','3','4']

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar([0.1, 0.9], y[:2], color=["#8AD6F4", "#CFEFFC"])
ax.bar([2.1, 2.9], y[2:], color=["#8AD6F4", "#CFEFFC"])
ax.bar(x, y, color=["#8AD6F4","#3EAEF4","#81E2DF","#CFEFFC"],label="Mujeres")
ax.bar(x, y, color=["#CFEFFC", "#12B687","#5EC160","#90E0AE"],label="Hombres")
ax.bar(x, y, color=["#8AD6F4", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#CFEFFC", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#8AD6F4","#CFEFFC","#8AD6F4","#CFEFFC"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 0.9, str(v), color='black', ha='center', va='bottom')  # Ajuste de la posición vertical

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Puntaje Obtenido según el género', fontsize = 16, pad=30)
ax.set_xticks(x)
ax.set_xticklabels(['                         Reprobaron','','                         Aprobaron',''])

plt.show()



# Puntaje y Colegio
# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

Oficial_Aprobaron= datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_naturaleza'] == 1)].shape[0]
Oficial_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_naturaleza'] == 1)].shape[0]
No_Oficial_Aprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_naturaleza'] == 0)].shape[0]
No_Oficial_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_naturaleza'] == 0)].shape[0]

y = [ Oficial_Reprobaron, No_Oficial_Reprobaron,Oficial_Aprobaron,No_Oficial_Aprobaron]
x = ['1','2','3','4']

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar([0.1, 0.9], y[:2], color=["#81E2DF", "#8bd3f8"])
ax.bar([2.1, 2.9], y[2:], color=["#81E2DF", "#8bd3f8"])
ax.bar(x, y, color=["#81E2DF","#3EAEF4","#81E2DF","#CFEFFC"],label="Oficial")
ax.bar(x, y, color=["#8bd3f8", "#12B687","#5EC160","#90E0AE"],label="No Oficial")
ax.bar(x, y, color=["#81E2DF", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#8bd3f8", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#81E2DF","#8bd3f8","#81E2DF","#8bd3f8"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 0.1, str(v), color='black', ha='center', va='bottom')  # Ajuste de la posición vertical

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Puntaje Obtenido según el colegio', fontsize = 16, pad=30)
ax.set_xticks(x)
ax.set_xticklabels(['                         Reprobaron','','                         Aprobaron',''])

plt.show()





#Graficos de pie
#Educacion madre
fig, ax = plt.subplots()
etiquetas = ["Primaria I","Primaria C","Secundaria I","Secundaria C",
             "Técnico I","Técnica C","Profesional I","Profesional C",
             "Postgrado","Ninguno","No Sabe","No Aplica"]

valores = [(datos["Educacion_Madre"]=='PI').sum(),(datos["Educacion_Madre"]=='PC').sum(),
           (datos["Educacion_Madre"]=='SBI').sum(),(datos["Educacion_Madre"]=='SBC').sum(),
           (datos["Educacion_Madre"]=='TI').sum(),(datos["Educacion_Madre"]=='TC').sum(),
           (datos["Educacion_Madre"]=='EPI').sum(),(datos["Educacion_Madre"]=='EPC').sum(),
           (datos["Educacion_Madre"]=='P').sum(),(datos["Educacion_Madre"]=='N').sum(),
           (datos["Educacion_Madre"]=='NS').sum(),(datos["Educacion_Madre"]=='NAP').sum()]

colores=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"]
ax.pie(valores, labels = None , autopct='%1.1f%%', textprops={'fontsize': 8}, pctdistance=0.7)
ax.legend(etiquetas, loc="right", bbox_to_anchor=(1.5, 0.5))
plt.title("Educación de la madre", fontsize = 16)
plt.show() 


#Educacion padre
fig, ax = plt.subplots()
etiquetas = ["Primaria I","Primaria C","Secundaria I","Secundaria C",
             "Técnico I","Técnica C","Profesional I","Profesional C",
             "Postgrado","Ninguno","No Sabe","No Aplica"]

valores = [(datos["Educacion_Padre"]=='PI').sum(),(datos["Educacion_Padre"]=='PC').sum(),
           (datos["Educacion_Padre"]=='SBI').sum(),(datos["Educacion_Padre"]=='SBC').sum(),
           (datos["Educacion_Padre"]=='TI').sum(),(datos["Educacion_Padre"]=='TC').sum(),
           (datos["Educacion_Padre"]=='EPI').sum(),(datos["Educacion_Padre"]=='EPC').sum(),
           (datos["Educacion_Padre"]=='P').sum(),(datos["Educacion_Padre"]=='N').sum(),
           (datos["Educacion_Padre"]=='NS').sum(),(datos["Educacion_Padre"]=='NAP').sum()]

colores=["#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"]
ax.pie(valores, labels = None , autopct='%1.1f%%', textprops={'fontsize': 8}, pctdistance=0.7)
ax.legend(etiquetas, loc="right", bbox_to_anchor=(1.5, 0.5))
plt.title("Educación de la madre", fontsize = 16)
plt.show() 


















#Histogramas

  ###                 Estrato
plt.hist(datos['fami_estratovivienda'], bins=5,color=("#81E2DF"))

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
#plt.gca().set_yticks([])
plt.ylim(0, 100000)


# Etiquetas y título
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma estrato de residencia', fontsize=16, pad=30)

# Mostrar el histograma
plt.show()

  ###                 Estrato









