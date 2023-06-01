
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
ax.set_title('Puntaje obtenido según el género', fontsize = 16, pad=30)
ax.set_xticks(x)
ax.set_xticklabels(['                         Reprobaron','','                         Aprobaron',''])

plt.show()







# Puntaje y Ubicación
# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

Urbano_Aprobaron= datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_area_ubicacion'] == 'URBANO')].shape[0]
Urbano_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_area_ubicacion'] == 'URBANO')].shape[0]
Rural_Aprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_area_ubicacion'] == 'RURAL')].shape[0]
Rural_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_area_ubicacion'] == 'RURAL')].shape[0]

y = [ Urbano_Reprobaron, Rural_Reprobaron,Urbano_Aprobaron,Rural_Aprobaron]
x = ['1','2','3','4']

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar([0.1, 0.9], y[:2], color=["#CCECFF", "#CCCCFF"])
ax.bar([2.1, 2.9], y[2:], color=["#CCECFF", "#CCCCFF"])
ax.bar(x, y, color=["#CCECFF","#3EAEF4","#81E2DF","#CFEFFC"],label="Urbano")
ax.bar(x, y, color=["#CCCCFF", "#12B687","#5EC160","#90E0AE"],label="Rural")
ax.bar(x, y, color=["#CCECFF", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#CCCCFF", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#CCECFF","#CCCCFF","#CCECFF","#CCCCFF"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 0.9, str(v), color='black', ha='center', va='bottom')  # Ajuste de la posición vertical

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Puntaje obtenido según la ubicación', fontsize = 16, pad=30)
ax.set_xticks(x)
ax.set_xticklabels(['                         Reprobaron','','                         Aprobaron',''])
plt.show()







# Puntaje y Colegio
# crear gráfica de barras
fig, ax = plt.subplots()
fig.subplots_adjust(top=1)

Oficial_Aprobaron= datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_naturaleza'] == "Oficial")].shape[0]
Oficial_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_naturaleza'] == "Oficial")].shape[0]
No_Oficial_Aprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['cole_naturaleza'] == "No_oficial")].shape[0]
No_Oficial_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['cole_naturaleza'] == "No_oficial")].shape[0]

y = [ Oficial_Reprobaron, No_Oficial_Reprobaron,Oficial_Aprobaron,No_Oficial_Aprobaron]
x = ['1','2','3','4']

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar([0.1, 0.9], y[:2], color=["#8AD6F4", "#CFEFFC"])
ax.bar([2.1, 2.9], y[2:], color=["#8AD6F4", "#CFEFFC"])
ax.bar(x, y, color=["#8AD6F4","#3EAEF4","#81E2DF","#CFEFFC"],label="Oficial")
ax.bar(x, y, color=["#CFEFFC", "#12B687","#5EC160","#90E0AE"],label="No Oficial")
ax.bar(x, y, color=["#8AD6F4", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#CFEFFC", "#12B687","#5EC160","#90E0AE"])
ax.bar(x, y, color=["#8AD6F4","#CFEFFC","#8AD6F4","#CFEFFC"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])

for i, v in enumerate(y):
    plt.text(i, v + 0.1, str(v), color='black', ha='center', va='bottom')  # Ajuste de la posición vertical

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Puntaje obtenido según el colegio', fontsize = 16, pad=30)
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

colores=["#6699FF","#99CCFF","#CCECFF","#33CCFF","#66FFCC","#CCFFCC","#99FF99","#CCFF99","#FFFF99",
         "#FFCC66","#FFCCCC","#FF9999"]
ax.pie(valores, labels = None ,colors=colores, autopct='%1.1f%%', textprops={'fontsize': 8}, pctdistance=0.7)
ax.legend(etiquetas, loc="right", bbox_to_anchor=(1.5, 0.5))
plt.title("Educación de la madre", fontsize = 15,pad=15)
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

colores=["#6699FF","#99CCFF","#CCECFF","#33CCFF","#66FFCC","#CCFFCC","#99FF99","#CCFF99","#FFFF99",
         "#FFCC66","#FFCCCC","#FF9999"]
ax.pie(valores, labels = None ,colors=colores, autopct='%1.1f%%', textprops={'fontsize': 8}, pctdistance=0.7)
ax.legend(etiquetas, loc="right", bbox_to_anchor=(1.5, 0.5))
plt.title("Educación del padre", fontsize = 15,pad=15)
plt.show() 







### Grafica de lineas
#Educacion madre

fig, ax = plt.subplots()
Educacion = ['PI','PC','SBI','SBC','EPI','EPC','TI','TC','P','N','NS','NAP']

PI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'PI')].shape[0]
PI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'PI')].shape[0]
PI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'PI')].shape[0]
PI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'PI')].shape[0]
PI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='PI')].shape[0]
PI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='PI')].shape[0]
PI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='PI')].shape[0]

PC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'PC')].shape[0]
PC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'PC')].shape[0]
PC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'PC')].shape[0]
PC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'PC')].shape[0]
PC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='PC')].shape[0]
PC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='PC')].shape[0]
PC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='PC')].shape[0]

SBI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'SBI')].shape[0]
SBI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'SBI')].shape[0]
SBI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'SBI')].shape[0]
SBI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'SBI')].shape[0]
SBI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='SBI')].shape[0]
SBI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='SBI')].shape[0]
SBI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='SBI')].shape[0]  

SBC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'SBC')].shape[0]
SBC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'SBC')].shape[0]
SBC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'SBC')].shape[0]
SBC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'SBC')].shape[0]
SBC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='SBC')].shape[0]
SBC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='SBC')].shape[0]
SBC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='SBC')].shape[0]  

EPI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'EPI')].shape[0]
EPI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'EPI')].shape[0]
EPI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'EPI')].shape[0]
EPI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'EPI')].shape[0]
EPI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='EPI')].shape[0]
EPI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='EPI')].shape[0]
EPI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='EPI')].shape[0]  

EPC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'EPC')].shape[0]
EPC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'EPC')].shape[0]
EPC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'EPC')].shape[0]
EPC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'EPC')].shape[0]
EPC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='EPC')].shape[0]
EPC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='EPC')].shape[0]
EPC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='EPC')].shape[0]  

TI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'TI')].shape[0]
TI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'TI')].shape[0]
TI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'TI')].shape[0]
TI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'TI')].shape[0]
TI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='TI')].shape[0]
TI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='TI')].shape[0]
TI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='TI')].shape[0]  

TC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'TC')].shape[0]
TC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'TC')].shape[0]
TC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'TC')].shape[0]
TC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'TC')].shape[0]
TC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='TC')].shape[0]
TC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='TC')].shape[0]
TC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='TC')].shape[0]  

P_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'P')].shape[0]
P_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'P')].shape[0]
P_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'P')].shape[0]
P_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'P')].shape[0]
P_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='P')].shape[0]
P_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='P')].shape[0]
P_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='P')].shape[0]  

N_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'N')].shape[0]
N_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'N')].shape[0]
N_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'N')].shape[0]
N_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'N')].shape[0]
N_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='N')].shape[0]
N_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='N')].shape[0]
N_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='N')].shape[0]  

NS_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'NS')].shape[0]
NS_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'NS')].shape[0]
NS_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'NS')].shape[0]
NS_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'NS')].shape[0]
NS_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='NS')].shape[0]
NS_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='NS')].shape[0]
NS_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='NS')].shape[0]  

NAP_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Madre"] == 'NAP')].shape[0]
NAP_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Madre"] == 'NAP')].shape[0]
NAP_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Madre"] == 'NAP')].shape[0]
NAP_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Madre"] == 'NAP')].shape[0]
NAP_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Madre"]=='NAP')].shape[0]
NAP_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Madre"]=='NAP')].shape[0]
NAP_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Madre"]=='NAP')].shape[0]  

valores = {'Estrato 0': [PI_0, PC_0, SBI_0, SBC_0, EPI_0, EPC_0, TI_0, TC_0, P_0, N_0, NS_0, NAP_0],
           'Estrato 1': [PI_1, PC_1, SBI_1, SBC_1, EPI_1, EPC_1, TI_1, TC_1, P_1, N_1, NS_1, NAP_1],
           'Estrato 2': [PI_2, PC_2, SBI_2, SBC_2, EPI_2, EPC_2, TI_2, TC_2, P_2, N_2, NS_2, NAP_2],
           'Estrato 3': [PI_3, PC_3, SBI_3, SBC_3, EPI_3, EPC_3, TI_3, TC_3, P_3, N_3, NS_3, NAP_3],
           'Estrato 4': [PI_4, PC_4, SBI_4, SBC_4, EPI_4, EPC_4, TI_4, TC_4, P_4, N_4, NS_4, NAP_4],
           'Estrato 5': [PI_5, PC_5, SBI_5, SBC_5, EPI_5, EPC_5, TI_5, TC_5, P_5, N_5, NS_5, NAP_5],
           'Estrato 6': [PI_6, PC_6, SBI_6, SBC_6, EPI_6, EPC_6, TI_6, TC_6, P_6, N_6, NS_6, NAP_6]}

colores=["#6699FF","#99CCFF","#66FFCC","#CCFFCC","#CCFF99","#FFFF99","#99FF99"]

for estrato, color in zip(valores.keys(), colores):
    ax.plot(Educacion, valores[estrato], marker='o', color=color, label=estrato)

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#plt.gca().set_yticks([])
#plt.ylim(0, 100000)
plt.title("Educacion del padre según el estrato", fontsize = 16,pad=30)
ax.legend()
plt.show()







#Educacion padre
fig, ax = plt.subplots()
Educacion = ['PI','PC','SBI','SBC','EPI','EPC','TI','TC','P','N','NS','NAP']

PI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'PI')].shape[0]
PI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'PI')].shape[0]
PI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'PI')].shape[0]
PI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'PI')].shape[0]
PI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='PI')].shape[0]
PI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='PI')].shape[0]
PI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='PI')].shape[0]

PC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'PC')].shape[0]
PC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'PC')].shape[0]
PC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'PC')].shape[0]
PC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'PC')].shape[0]
PC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='PC')].shape[0]
PC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='PC')].shape[0]
PC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='PC')].shape[0]

SBI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
SBI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
SBI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
SBI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
SBI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='SBI')].shape[0]
SBI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='SBI')].shape[0]
SBI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='SBI')].shape[0]  

SBC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
SBC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
SBC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
SBC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
SBC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='SBC')].shape[0]
SBC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='SBC')].shape[0]
SBC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='SBC')].shape[0]  

EPI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
EPI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
EPI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
EPI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
EPI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='EPI')].shape[0]
EPI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='EPI')].shape[0]
EPI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='EPI')].shape[0]  

EPC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
EPC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
EPC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
EPC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
EPC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='EPC')].shape[0]
EPC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='EPC')].shape[0]
EPC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='EPC')].shape[0]  

TI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'TI')].shape[0]
TI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'TI')].shape[0]
TI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'TI')].shape[0]
TI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'TI')].shape[0]
TI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='TI')].shape[0]
TI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='TI')].shape[0]
TI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='TI')].shape[0]  

TC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'TC')].shape[0]
TC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'TC')].shape[0]
TC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'TC')].shape[0]
TC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'TC')].shape[0]
TC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='TC')].shape[0]
TC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='TC')].shape[0]
TC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='TC')].shape[0]  

P_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'P')].shape[0]
P_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'P')].shape[0]
P_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'P')].shape[0]
P_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'P')].shape[0]
P_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='P')].shape[0]
P_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='P')].shape[0]
P_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='P')].shape[0]  

N_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'N')].shape[0]
N_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'N')].shape[0]
N_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'N')].shape[0]
N_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'N')].shape[0]
N_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='N')].shape[0]
N_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='N')].shape[0]
N_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='N')].shape[0]  

NS_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'NS')].shape[0]
NS_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'NS')].shape[0]
NS_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'NS')].shape[0]
NS_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'NS')].shape[0]
NS_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='NS')].shape[0]
NS_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='NS')].shape[0]
NS_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='NS')].shape[0]  

NAP_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
NAP_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
NAP_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
NAP_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
NAP_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='NAP')].shape[0]
NAP_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='NAP')].shape[0]
NAP_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='NAP')].shape[0]  

valores = {'Estrato 0': [PI_0, PC_0, SBI_0, SBC_0, EPI_0, EPC_0, TI_0, TC_0, P_0, N_0, NS_0, NAP_0],
           'Estrato 1': [PI_1, PC_1, SBI_1, SBC_1, EPI_1, EPC_1, TI_1, TC_1, P_1, N_1, NS_1, NAP_1],
           'Estrato 2': [PI_2, PC_2, SBI_2, SBC_2, EPI_2, EPC_2, TI_2, TC_2, P_2, N_2, NS_2, NAP_2],
           'Estrato 3': [PI_3, PC_3, SBI_3, SBC_3, EPI_3, EPC_3, TI_3, TC_3, P_3, N_3, NS_3, NAP_3],
           'Estrato 4': [PI_4, PC_4, SBI_4, SBC_4, EPI_4, EPC_4, TI_4, TC_4, P_4, N_4, NS_4, NAP_4],
           'Estrato 5': [PI_5, PC_5, SBI_5, SBC_5, EPI_5, EPC_5, TI_5, TC_5, P_5, N_5, NS_5, NAP_5],
           'Estrato 6': [PI_6, PC_6, SBI_6, SBC_6, EPI_6, EPC_6, TI_6, TC_6, P_6, N_6, NS_6, NAP_6]}

"""colores=["#6699FF","#99CCFF","#CCECFF","#33CCFF","#66FFCC","#CCFFCC","#99FF99","#CCFF99","#FFFF99",
         "#FFCC66","#FFCCCC","#FF9999"]
    for estrato, valores_educacion in valores.items():
    ax.plot(Educacion, valores_educacion,colors=colores, marker='o', label=estrato)
    
    """
    
colores=["#6699FF","#99CCFF","#66FFCC","#CCFFCC","#CCFF99","#FFFF99","#99FF99"]

for estrato, color in zip(valores.keys(), colores):
    ax.plot(Educacion, valores[estrato], marker='o', color=color, label=estrato)
    
# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#plt.gca().set_yticks([])
#plt.ylim(0, 100000)

plt.title("Educacion del padre según el estrato", fontsize = 16,pad=30)
ax.legend()
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









