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


def estimar(radio1,radio2,radio3, dropdown1, dropdown2, dropdown3, dropdown4):

    Sex=9
    if radio1 == 'F':
       Sex="1"
    elif radio1 ==  'M':
       Sex="0"
   
    Ubicacion=9
    if radio2 == 'URBANO':
       Ubicacion="1"
    elif radio2 ==  'RURAL':
       Ubicacion="0"
     
    Colegio=9
    if radio3 == 'OFICIAL':
       Colegio="1"
    elif radio3 ==  'NO OFICIAL':
       Colegio="0"   
    
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
    if dropdown2 == "Poco":
        Per_Hogar = "0"
    elif dropdown2 == "Medio":
        Per_Hogar= "1"
    elif dropdown2 == "Alto":
        Per_Hogar = "2"
       
        
    Edu_madre = 9
    if dropdown3 == "EPC":
        Edu_madre = "1"
    elif dropdown3 == "PC":
        Edu_madre= "2"
    elif dropdown3 == "EPI":
        Edu_madre= "3"
    elif dropdown3 == "SBC":
        Edu_madre= "4"
    elif dropdown3 == "SBI":
        Edu_madre= "5"
    elif dropdown3 == "NS":
        Edu_madre= "6"
    elif dropdown3 == "TI":
        Edu_madre= "7"
    elif dropdown3 == "TC":
        Edu_madre= "8"
    elif dropdown3 == "N":
        Edu_madre= "9"
    elif dropdown3 == "PI":
        Edu_madre= "10"
    elif dropdown3 == "P":
        Edu_madre= "11"
    elif dropdown3 == "NA":
        Edu_madre= "0 "
        
        
    Edu_padre = 9
    if dropdown4 == "EPC":
        Edu_padre = "1"
    elif dropdown4 == "PC":
        Edu_padre= "2"
    elif dropdown4 == "EPI":
        Edu_padre= "3"
    elif dropdown4 == "SBC":
        Edu_padre= "4"
    elif dropdown4 == "SBI":
        Edu_padre= "5"
    elif dropdown4 == "NS":
        Edu_padre= "6"
    elif dropdown4 == "TI":
        Edu_padre= "7"
    elif dropdown4 == "TC":
        Edu_padre= "8"
    elif dropdown4 == "N":
        Edu_padre= "9"
    elif dropdown4 == "PI":
        Edu_padre= "10"
    elif dropdown4 == "P":
        Edu_padre= "11"
    elif dropdown4 == "NA":
        Edu_padre= "0 "   
        
      
    modelo = BIFReader("Modelo.bif").get_model()
    inferencia = VariableElimination(modelo)
    evidencia = {}
    
   
    
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
    html.Div(" 2. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar', el cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 3. Finalmente, se mostrará un resumen de los datos, debajo de este, encontrarás gráficas de tu interés y el resultado."),
    
    html.Br(),
    
     html.Div(["Sexo del estudiante: ",
                dcc.RadioItems(
                id='Radio-1',
                options=[{'label': i, 'value': i} for i in ['Femenino', 'Masculino']],
                labelStyle={'display': 'inline-block'}), 
                html.Br()],
                style={'display': 'inline-block','width': '22%'}),
     
     html.Div(["Área de ubicación: ",
              dcc.Dropdown(
                id='Radio-2',
                options=[{'label': i, 'value': i} for i in ["Urbano","Rural"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    html.Div(["Categoría del Colegio: ",
              dcc.Dropdown(
                id='Radio-3',
                options=[{'label': i, 'value': i} for i in ["Oficial","No Oficial"]],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    html.Div(["Estrato de residencia del estudiante: ",
              dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in ['Estrato 1','Estrato 2','Estrato 3','Estrato 4','Estrato 5','Estrato 6','Sin Estrato']],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    html.Div(["Área de ubicación: ",
              dcc.Dropdown(
                id='dropdown-2',
                options=[{'label': i, 'value': i} for i in ["Urbano","Rural"]],value="Seleccione"),
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
    

    