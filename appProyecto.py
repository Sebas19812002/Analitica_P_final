import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import base64
import Funciones as F
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server




#-----------------connect to DB----------------------#
datos = F.Conexion_DB_()
# datos = pd.read_csv("datos_filtrados.csv")
print(datos.head())
#------------------Graficas--------------------------------#

#################################################################################################
#Imagenes de exploracion


imagen_bienvenida='IMG_Inicio.png'
encoded_image = base64.b64encode(open(imagen_bienvenida, 'rb').read())
image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})


#################################################################################################
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

Estrato_0 = [PI_0, PC_0, SBI_0, SBC_0, EPI_0, EPC_0, TI_0, TC_0, P_0, N_0, NS_0, NAP_0]
Estrato_1 = [PI_1, PC_1, SBI_1, SBC_1, EPI_1, EPC_1, TI_1, TC_1, P_1, N_1, NS_1, NAP_1]
Estrato_2 = [PI_2, PC_2, SBI_2, SBC_2, EPI_2, EPC_2, TI_2, TC_2, P_2, N_2, NS_2, NAP_2]
Estrato_3 = [PI_3, PC_3, SBI_3, SBC_3, EPI_3, EPC_3, TI_3, TC_3, P_3, N_3, NS_3, NAP_3]
Estrato_4 = [PI_4, PC_4, SBI_4, SBC_4, EPI_4, EPC_4, TI_4, TC_4, P_4, N_4, NS_4, NAP_4]
Estrato_5 = [PI_5, PC_5, SBI_5, SBC_5, EPI_5, EPC_5, TI_5, TC_5, P_5, N_5, NS_5, NAP_5]
Estrato_6 = [PI_6, PC_6, SBI_6, SBC_6, EPI_6, EPC_6, TI_6, TC_6, P_6, N_6, NS_6, NAP_6]

colores=["#6699FF","#99CCFF","#66FFCC","#CCFFCC","#CCFF99","#FFFF99","#99FF99"]

trazo_0 = go.Scatter(x=Educacion, y=Estrato_0, mode='lines+markers', name='No Sabe/Ninguno')
trazo_1 = go.Scatter(x=Educacion, y=Estrato_1, mode='lines+markers', name='Estrato 1')
trazo_2 = go.Scatter(x=Educacion, y=Estrato_2, mode='lines+markers', name='Estrato 2')
trazo_3 = go.Scatter(x=Educacion, y=Estrato_3, mode='lines+markers', name='Estrato 3')
trazo_4 = go.Scatter(x=Educacion, y=Estrato_4, mode='lines+markers', name='Estrato 4')
trazo_5 = go.Scatter(x=Educacion, y=Estrato_5, mode='lines+markers', name='Estrato 5')
trazo_6 = go.Scatter(x=Educacion, y=Estrato_6, mode='lines+markers', name='Estrato 6')
#################################################################################################

HPI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'PI')].shape[0]
HPI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'PI')].shape[0]
HPI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'PI')].shape[0]
HPI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'PI')].shape[0]
HPI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='PI')].shape[0]
HPI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='PI')].shape[0]
HPI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='PI')].shape[0]

HPC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'PC')].shape[0]
HPC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'PC')].shape[0]
HPC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'PC')].shape[0]
HPC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'PC')].shape[0]
HPC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='PC')].shape[0]
HPC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='PC')].shape[0]
HPC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='PC')].shape[0]

HSBI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
HSBI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
HSBI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
HSBI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'SBI')].shape[0]
HSBI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='SBI')].shape[0]
HSBI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='SBI')].shape[0]
HSBI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='SBI')].shape[0]  

HSBC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
HSBC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
HSBC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
HSBC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'SBC')].shape[0]
HSBC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='SBC')].shape[0]
HSBC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='SBC')].shape[0]
HSBC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='SBC')].shape[0]  

HEPI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
HEPI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
HEPI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
HEPI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'EPI')].shape[0]
HEPI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='EPI')].shape[0]
HEPI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='EPI')].shape[0]
HEPI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='EPI')].shape[0]  

HEPC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
HEPC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
HEPC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
HEPC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'EPC')].shape[0]
HEPC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='EPC')].shape[0]
HEPC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='EPC')].shape[0]
HEPC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='EPC')].shape[0]  

HTI_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'TI')].shape[0]
HTI_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'TI')].shape[0]
HTI_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'TI')].shape[0]
HTI_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'TI')].shape[0]
HTI_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='TI')].shape[0]
HTI_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='TI')].shape[0]
HTI_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='TI')].shape[0]  

HTC_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'TC')].shape[0]
HTC_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'TC')].shape[0]
HTC_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'TC')].shape[0]
HTC_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'TC')].shape[0]
HTC_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='TC')].shape[0]
HTC_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='TC')].shape[0]
HTC_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='TC')].shape[0]  

HP_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'P')].shape[0]
HP_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'P')].shape[0]
HP_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'P')].shape[0]
HP_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'P')].shape[0]
HP_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='P')].shape[0]
HP_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='P')].shape[0]
HP_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='P')].shape[0]  

HN_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'N')].shape[0]
HN_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'N')].shape[0]
HN_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'N')].shape[0]
HN_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'N')].shape[0]
HN_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='N')].shape[0]
HN_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='N')].shape[0]
HN_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='N')].shape[0]  

HNS_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'NS')].shape[0]
HNS_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'NS')].shape[0]
HNS_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'NS')].shape[0]
HNS_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'NS')].shape[0]
HNS_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='NS')].shape[0]
HNS_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='NS')].shape[0]
HNS_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='NS')].shape[0]  

HNAP_0 = datos.loc[(datos['fami_estratovivienda'] == 0) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
HNAP_1 = datos.loc[(datos['fami_estratovivienda'] == 1) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
HNAP_2 = datos.loc[(datos['fami_estratovivienda'] == 2) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
HNAP_3 = datos.loc[(datos['fami_estratovivienda'] == 3) & (datos["Educacion_Padre"] == 'NAP')].shape[0]
HNAP_4= datos.loc[(datos['fami_estratovivienda'] == 4) & (datos["Educacion_Padre"]=='NAP')].shape[0]
HNAP_5= datos.loc[(datos['fami_estratovivienda'] == 5) & (datos["Educacion_Padre"]=='NAP')].shape[0]
HNAP_6= datos.loc[(datos['fami_estratovivienda'] == 6) & (datos["Educacion_Padre"]=='NAP')].shape[0]  

HEstrato_0 = [HPI_0, HPC_0, HSBI_0, HSBC_0, HEPI_0, HEPC_0, HTI_0, HTC_0, HP_0, HN_0, HNS_0, HNAP_0]
HEstrato_1 = [HPI_1, HPC_1, HSBI_1, HSBC_1, HEPI_1, HEPC_1, HTI_1, HTC_1, HP_1, HN_1, HNS_1, HNAP_1]
HEstrato_2 = [HPI_2, HPC_2, HSBI_2, HSBC_2, HEPI_2, HEPC_2, HTI_2, HTC_2, HP_2, HN_2, HNS_2, HNAP_2]
HEstrato_3 = [HPI_3, HPC_3, HSBI_3, HSBC_3, HEPI_3, HEPC_3, HTI_3, HTC_3, HP_3, HN_3, HNS_3, HNAP_3]
HEstrato_4 = [HPI_4, HPC_4, HSBI_4, HSBC_4, HEPI_4, HEPC_4, HTI_4, HTC_4, HP_4, HN_4, HNS_4, HNAP_4]
HEstrato_5 = [HPI_5, HPC_5, HSBI_5, HSBC_5, HEPI_5, HEPC_5, HTI_5, HTC_5, HP_5, HN_5, HNS_5, HNAP_5]
HEstrato_6 = [HPI_6, HPC_6, HSBI_6, HSBC_6, HEPI_6, HEPC_6, HTI_6, HTC_6, HP_6, HN_6, HNS_6, HNAP_6]

Htrazo_0 = go.Scatter(x=Educacion, y=HEstrato_0, mode='lines+markers', name='No Sabe/Ninguno')
Htrazo_1 = go.Scatter(x=Educacion, y=HEstrato_1, mode='lines+markers', name='Estrato 1')
Htrazo_2 = go.Scatter(x=Educacion, y=HEstrato_2, mode='lines+markers', name='Estrato 2')
Htrazo_3 = go.Scatter(x=Educacion, y=HEstrato_3, mode='lines+markers', name='Estrato 3')
Htrazo_4 = go.Scatter(x=Educacion, y=HEstrato_4, mode='lines+markers', name='Estrato 4')
Htrazo_5 = go.Scatter(x=Educacion, y=HEstrato_5, mode='lines+markers', name='Estrato 5')
Htrazo_6 = go.Scatter(x=Educacion, y=HEstrato_6, mode='lines+markers', name='Estrato 6')

#############################################################################################################
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
plt.savefig('Puntaje_y_genero.png')








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
plt.savefig('Puntaje_y_ubicacion.png')







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

plt.savefig('Puntaje_y_colegio.png')

########################################################################################################################3

fig_m = go.Figure(data=[trazo_0, trazo_1, trazo_2, trazo_3, trazo_4, trazo_5, trazo_6])
fig_h = go.Figure(data=[Htrazo_0, Htrazo_1, Htrazo_2, Htrazo_3, Htrazo_4, Htrazo_5, Htrazo_6])


tab1=dcc.Tab(label='Información de la madre',children=[
    html.Div('En esta pestaña se encuentra una gráfica dinámica, la cual contiene información del estrato según la educación de la madre.'),
    html.Br(),
    
    html.H6('Educación de la Madre', style={'text-align': 'center', 'margin-bottom': '10px'}),

    dcc.Graph(id='line-chart-madre', figure=fig_m,
        config={'displayModeBar': False},  # Oculta la barra de herramientas de la gráfica
        style={'backgroundColor': 'rgba(0,0,0,0)'}  # Establece el color de fondo transparente
    )
    
       
])

tab2=dcc.Tab(label='Información del padre',children=[
    html.Div('En esta pestaña se encuentra una gráfica dinámica, la cual contiene información del estrato según la educación del padre.'),
    html.Br(),
    html.H6('Educación del Padre', style={'text-align': 'center'}),
    html.Br(),
    dcc.Graph(id='line-chart-padre', figure=fig_h,
        config={'displayModeBar': False},  # Oculta la barra de herramientas de la gráfica
        style={'backgroundColor': 'rgba(0,0,0,0)'}  # Establece el color de fondo transparente
    ) 
])

Exploracion1='Puntaje_y_genero.png'
encoded_image = base64.b64encode(open(Exploracion1, 'rb').read())
exp1 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})

Exploracion2='Puntaje_y_ubicacion.png'
encoded_image = base64.b64encode(open(Exploracion2, 'rb').read())
exp2 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})


Exploracion3='Puntaje_y_colegio.png'
encoded_image = base64.b64encode(open(Exploracion3, 'rb').read())
exp3 = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'inline-block', 'margin-right': '10px','width': '30%', 'float': 'left'})





tab3=dcc.Tab(label='Información de la muestra',children=[
    html.Div('En esta pestaña se encuentran gráficas asociadas a la muestra en general.'),
    html.Br(),
    html.Div(exp1),
    html.Div(exp2),
    html.Div(exp3)
])



pestanas = [tab1, tab2, tab3]
tabs = dcc.Tabs(children=pestanas)



app.layout = html.Div([
    html.Div(children=[image]),
    html.Br(),
    html.H6(''' Para hacer uso del sistema de datos es necesario realizar lo siguiente:'''),
    html.Div(" 1. Asegurate de ingresar los datos correctamente en las casillas correspondientes, en caso de que no poseas el dato puedes dejar la casilla en blanco."),
    html.Div(" 2. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar', el cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 3. Finalmente, se mostrará un resumen de los datos, debajo de este, encontrarás gráficas de tu interés y el resultado."),
    
    html.Br(),
    
    html.Div(["Para iniciar, porfavor seleccione que tipo de modelo prefiere: ",
                dcc.RadioItems(
                id='Radio-4',
                options=[{'label': i, 'value': i} for i in [ 'Modelo Normal','Modelo Suavizado']],
                labelStyle={'display': 'inline-block'},value='Modelo Normal'), 
                html.Br()]),
    
     html.Div(["Genero del estudiante: ",
                dcc.RadioItems(
                id='Radio-1',
                options=[{'label': i, 'value': i} for i in ['Femenino', 'Masculino']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
     
     html.Div(["Área de ubicación: ",
              dcc.RadioItems(
                id='Radio-2',
                options=[{'label': i, 'value': i} for i in ["Urbano","Rural"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    html.Br(),
    
    html.Div(["Categoría del Colegio: ",
              dcc.RadioItems(
                id='Radio-3',
                options=[{'label': i, 'value': i} for i in ["Oficial","No Oficial"]],value="Seleccione"),
                html.Br()],
                style={'margin-right': '10px','width': '22%', 'float': 'left'}),
    
    html.Div(["Estrato de residencia del estudiante: ",
              dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in ['Estrato 1','Estrato 2','Estrato 3','Estrato 4','Estrato 5','Estrato 6','Sin Estrato']],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    html.Div(["Número de personas en la vivienda: ",
              dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in ["1 a 4","5 a 6","Más de 7"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}), 
    html.Br(),
    html.Div(["Educación de la madre: ",
              dcc.Dropdown(
                id='dropdown-3',
                options=[{'label': i, 'value': i} for i in ['Primaria incompleta','Primaria completa',
                                                            'Secundaria (Bachillerato) incompleta','Secundaria (Bachillerato) completa',
                                                            'Técnica o tecnológica incompleta','Técnica o tecnológica completa',
                                                            'Educación profesional incompleta' ,'Educación profesional completa',
                                                            'Postgrado','No sabe','Ninguno' ,'No Aplica']],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    html.Div(["Educación del padre: ",
              dcc.Dropdown(
                id='dropdown-4',
                options=[{'label': i, 'value': i} for i in ['Primaria incompleta','Primaria completa',
                                                            'Secundaria (Bachillerato) incompleta','Secundaria (Bachillerato) completa',
                                                            'Técnica o tecnológica incompleta','Técnica o tecnológica completa',
                                                            'Educación profesional incompleta' ,'Educación profesional completa',
                                                            'Postgrado','No sabe','Ninguno' ,'No Aplica']],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
    html.Br(),      
    html.Br(),
    html.Br(),
    html.Button('Continuar', id='button', n_clicks=0,style={'marginLeft': 'auto', 'marginRight': 'auto','text-align': 'center'}),
    html.Button('Vaciar todo', id='reset-button',n_clicks=0,style={'marginLeft': 'auto', 'marginRight': 'auto','text-align': 'center'}),

    html.Div(id='alert-container'),
    html.Div(id='output'),
    html.Br(),
    html.Br(),   
    
    html.H6(''' Visualizaciones:'''),
    html.Div("A continuación, tienes a tu disposición algunas visualizaciones que pueden ser de tu interés, al igual que el resultado obtenido."),
    html.Br(),
    
    tabs,
    
    
    html.Br(),
    html.Br(),   
    
    ])



@app.callback(
    Output('output', 'children'),
    Input('button', 'n_clicks'),
    State('Radio-1', 'value'),
    State('Radio-2', 'value'),
    State('Radio-3', 'value'),
    State('Radio-4', 'value'),
    State('dropdown-1', 'value'),
    State('dropdown-2', 'value'),
    State('dropdown-3', 'value'),
    State('dropdown-4', 'value'))

def validate_selection (n_clicks,radio1,radio2,radio3,radio4, dropdown1, dropdown2, dropdown3, dropdown4):
    
    if n_clicks > 0 != None :
        resultado=F.estimar(radio1,radio2, radio3,radio4, dropdown1, dropdown2, dropdown3, dropdown4)
        tabla=html.Table([
                html.Tr([
                    html.Td(''),
                    html.Td('Probabilidad de ser aceptado'),
                    html.Td('Probabilidad de ser rechazado')
                ]),

                html.Tr([
                 
                    html.Td(f"{round(resultado[0],2)*100}%", style={'text-align': 'center'}),
                    html.Td(f"{round(resultado[1],2)*100}%", style={'text-align': 'center'})
                ])],
                style={'marginLeft': 'auto', 'marginRight': 'auto'})
        tabla1=html.Table([
                html.Tr([
                    html.Td('Modelo:  '),
                    html.Td(radio4)
                ]),
                html.Tr([
                    html.Td('Genero del estudiante: '),
                    html.Td(radio1)
                ]),
                html.Tr([
                    html.Td('Área de ubicación: '),
                    html.Td(radio2)
                ]),
                html.Tr([
                    html.Td('Categoría del Colegio: '),
                    html.Td(radio3)
                ]),
                html.Tr([
                    html.Td('Estrato de residencia del estudiante: '),
                    html.Td(dropdown1)
                ]),
                html.Tr([
                    html.Td('Número de personas en la vivienda: '),
                    html.Td(dropdown2)
                ]),
                html.Tr([
                    html.Td('Educación de la madre: '),
                    html.Td(dropdown3)
                ]),
                html.Tr([
                    html.Td('Educación del padre: '),
                    html.Td(dropdown4)
                ]),
                
               ],
                style={'marginLeft': 'auto', 'marginRight': 'auto'})

        
        return (html.Div(html.H5(["A Continuación se mostrará la información ingresada:", 
                        html.Br()],style={'color': 'green'})),
                
                html.Br(),
               
                tabla1,
                html.Br(),
               
                html.Div(html.H5(["De acuerdo al puntaje se espera:", 
                        html.Br()],style={'color': 'green'})),

                tabla,
                html.Br(),
            
               )
             
@app.callback(
    Output('Radio-1', 'value'),
    Output('Radio-2', 'value'),
    Output('Radio-3', 'value'),
    Output('dropdown-1', 'value'),
    Output('dropdown-2', 'value'),
    Output('dropdown-3', 'value'),
    Output('dropdown-4', 'value'),
    Input('reset-button', 'n_clicks')
    )
def reset_btn(n_clicks):
    if n_clicks>0:
        return (None,None,None,'No aplica','No aplica','No aplica','No aplica')
    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)
    
