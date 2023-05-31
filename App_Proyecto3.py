import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd
import base64


#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
#print(df.columns)

#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#Definir las opciones de seleccion
def estimar(dropdown1):   
    
    genero = 9
    if dropdown1 == "Entre 29 y 39 años":
        genero = "1"
    elif dropdown1 == "Entre 40 y 54 años":
        genero = "2"
    elif dropdown1 == "Entre 55 y 64 años":
        genero = "3"
    elif dropdown1 == "Entre 65 y 79 años":
        genero ="4"
    
    return resultado


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

    html.Div(children='''
        Histograma de casos presentes en la dificultad de las materia de Ingeniería Industrial
    '''),
    html.Br(),
    

    

    
     
    
    html.Div(["Rango de edad del paciente: ",
              dcc.Dropdown(
                id='dropdown-1',
                options=[{'label': i, 'value': i} for i in Edad],value="Seleccione"),
                html.Br()],
                style={'display': 'inline-block', 'margin-right': '10px','width': '22%', 'float': 'left', 'display': 'inline-block'}),
   
    
    
    
    
    
    
    
    
    
    
    tabs
    ])

if __name__ == '__main__':
    app.run_server(debug=True)



    
    
    