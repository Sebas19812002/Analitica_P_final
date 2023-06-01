
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

Mujeres_Aprobaron= datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['estu_genero'] == 'F')].shape[0]
Mujeres_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['estu_genero'] == 'F')].shape[0]
Hombres_Aprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Aceptado') & (datos['estu_genero'] == 'M')].shape[0]
Hombres_Reprobaron = datos.loc[(datos['Puntaje_obtenido'] == 'Rechazado') & (datos['estu_genero'] == 'M')].shape[0]

y = [ Mujeres_Reprobaron, Hombres_Reprobaron,Mujeres_Aprobaron,Hombres_Aprobaron]
x = ['1','2','3','4']

#ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE","#CFEFFC", "#8AD6F4","#3EAEF4","#81E2DF"],label="Adultos")
ax.bar([0.1, 0.9], y[:2], color=["#D7F47C", "#12B687"])
ax.bar([2.1, 2.9], y[2:], color=["#5EC160", "#90E0AE"])
ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE"],label="Muje")
ax.bar(x, y, color=["#12B687", "#12B687","#5EC160","#90E0AE"],label="Adultos Mayores")
ax.bar(x, y, color=["#5EC160", "#12B687","#5EC160","#90E0AE"],label="Tercera Edad")
ax.bar(x, y, color=["#90E0AE", "#12B687","#5EC160","#90E0AE"],label="Jovenes")
ax.bar(x, y, color=["#D7F47C", "#12B687","#5EC160","#90E0AE"])

# quitar los bordes del gráfico y los valores del eje y
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().set_yticks([])
plt.ylim(0, 150000)

for i, v in enumerate(y):
    plt.text(i, v + 5, str(v), color='black', ha='center', va='bottom')  # Ajuste de la posición vertical

# agregar leyenda
ax.legend(loc="upper center", bbox_to_anchor=[0.5,-0.1], ncol=4)
ax.set_title('Edad de las mujeres de la muestra', fontsize = 18)
ax.set_xticks(x)
ax.set_xticklabels(['                         Reprobaron','','                         Aprobaron',''])

plt.show()












