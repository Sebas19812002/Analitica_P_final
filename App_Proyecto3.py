import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import dcc  # dash core components
from dash import html # dash html components
import pandas as pd
import base64
from pgmpy.estimators import BayesianEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.readwrite import BIFReader


def estimar(radio1, dropdown1, dropdown2):

    Sex=9
    if radio1 == 'Hombre':
       Sex="1"
    elif radio1 ==  'Mujer':
       Sex="0"
   
    edad = 9
    if dropdown1 == "Entre 29 y 39 años":
        edad = "1"
    elif dropdown1 == "Entre 40 y 54 años":
            edad = "2"
    elif dropdown1 == "Entre 55 y 64 años":
        edad = "3"
    elif dropdown1 == "Entre 65 y 79 años":
        edad ="4"
    
    CP = 9
    if dropdown2 == 'Angina típica':
        CP = "1"
    elif dropdown2 == 'Angina atípica':
        CP = "2"
    elif dropdown2 == 'Dolor no anginoso':
        CP = "3"
    elif dropdown2 == 'Asintomático':
        CP = "4"
    

   
    modelo = BIFReader("Modelo.bif").get_model()
    inferencia = VariableElimination(modelo)
    evidencia = {}
    
    if Sex !=9: 
        evidencia["sex"]= Sex
   
    if edad !=9: 
        evidencia["age"]= edad
  
    if CP !=9: 
        evidencia["cpt"]= CP
   
    
    resultado = inferencia.query(['diagnosis'],evidence=evidencia).values
    return resultado

#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


#############################################################################################
#Creación de las visualizaciones


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#############################################################################################

#Cargar una imagen desde el computador
imagen_bienvenida='IMG_Inicio.png'
encoded_image = base64.b64encode(open(imagen_bienvenida, 'rb').read())
image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})


tab1=dcc.Tab(label='Análisis de la muestra',children=[
    html.Div('En esta pestaña se encuentra información sobre la distribucón de la muestra de datos'),
    html.Br()
])

tab2=dcc.Tab(label='Resultados',children=[
    html.Div('En esta pestaña se encuentra información relacionada con la información que usted desea conocer'),
    html.Br()
])

pestanas = [tab1, tab2]
tabs = dcc.Tabs(children=pestanas)








app.layout = html.Div([
    html.Div(children=[image]),
    
    html.H6(''' Para hacer uso del sistema de datos es necesario realizar lo siguiente:'''),
    html.Div(" 1. Asegurate de ingresar los datos correctamente en las casillas correspondientes, en caso de que no poseas el dato puedes dejar la casilla en blanco."),
    html.Div(''' 2. Debes ingresar al menos información del género y la edad del paciente para poder generar el resultado. Ten en cuenta que entre más información indiques, más acertada será la valoración.'''),
    html.Div(" 3. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar' en cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 4. Luego, fijate de haber completado todos los datos y que el sistema no haya arrojado una alerta, de ser asi, la encontrarás de color rojo debajo del boyon 'Continuar'"),
    
    html.Br(),
    
     html.Div(["Sexo del estudiante: ",
                dcc.RadioItems(
                id='Radio-1',
                options=[{'label': i, 'value': i} for i in ['Hombre', 'Mujer']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block','width': '22%'}
                ),
     
     html.Div(["Área de ubicación: ",
              dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in ["Rural","Urbano"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    
    html.Div(["Nacionalidad del estudiante: ",
              dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in ["FALTA"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
  
    html.Br(),
    html.Button('Continuar', id='button', n_clicks=0),
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
    State('dropdown-1', 'value'),
    State('dropdown-2', 'value')
    )
    
def validate_selection (n_clicks,radio1,dropdown1,dropdown2):
    
    if n_clicks > 0 and radio1 is None or n_clicks > 0 and dropdown1 == "Seleccione" or n_clicks > 0 and dropdown1 is None:
        if radio1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado el genero del paciente',style={'color': 'red'})
                                    ]))
        elif dropdown1 == "Seleccione" or dropdown1 is None:
            return html.H5(html.Div([html.Div('Por favor, asegurate de haber ingresado la edad del paciente', style={'color': 'red'})
                                     ]))

    
    elif n_clicks > 0 and radio1 is not None  and dropdown1 != "Seleccione" and dropdown2 != "Seleccione"  :   
        tabla=html.Table([
                html.Tr([
                    html.Td(''),
                    html.Td('Probabilidad de NO tener la enfermedad'),
                    html.Td('Probabilidad de SI tener la enfermedad')
                ]),
                

                html.Tr([
                    html.Td('En ese sentido, tu resultado es:'),
                    html.Td(f"{round(estimar(radio1, dropdown1, dropdown2)[0],3)}", style={'text-align': 'center'}),
                    html.Td(f"{round(estimar(radio1, dropdown1, dropdown2)[0],3)}", style={'text-align': 'center'})
                ])])
        
        return (html.Div(html.H5(["A Continuación se mostrará la información ingresada:", 
                        html.Br()],style={'color': 'green'})),
               html.Div([f"·    Rango de edad del paciente -----------------------------------------> {dropdown1}", 
                        html.Br()],style={'color': 'black'}),
               
               
               html.Div([f"·    Indique el sexo del paciente -------------------------------------------> {radio1}", 
                        html.Br()],style={'color': 'black'}),
               
                             
               html.Br(),
               
               tabla
              
               
               )






if __name__ == '__main__':
    app.run_server(debug=True)
    

    