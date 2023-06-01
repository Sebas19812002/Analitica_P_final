import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import base64
import Funciones as F
import plotly.graph_objs as go

#http://127.0.0.1:8050/ 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server




#-----------------connect to DB----------------------#
#datos=F.Conexion_DB_()
#------------------Graficas--------------------------------#
#F.crear_visualizaciones(datos)

#################################################################################################
#Imagenes de exploracion


imagen_bienvenida='IMG_Inicio.png'
encoded_image = base64.b64encode(open(imagen_bienvenida, 'rb').read())
image = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
    style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})


tab1=dcc.Tab(label='Análisis de la muestra',children=[
    html.Div('En esta pestaña se encuentra información sobre la distribucón de la muestra de datos.'),
    html.Br(),
    
    html.H6('Educacion Madre', style={'float': 'left', 'width': '50%', 'text-align': 'center'}),
    html.H6('Educacion Padre', style={'float': 'right', 'width': '50%', 'text-align': 'center'}),
    
    html.Br(),
    
    
    html.Div(["Si desea ver un estrato en particular seleccionelo en la casilla: ",
              dcc.Dropdown(
                id='dropdown-5',
                options=[{'label': i, 'value': i} for i in ["No Sabe/Ninguno","Estrato 1","Estrato 2","Estrato 3",
                                                            "Estrato 4","Estrato 5","Estrato 6","Todos"]],value="Todos"),
                html.Br()],
                style={'display': 'inline-block', 'margin-left': '10px','margin-right': '20px','width': '45%', 'float': 'left', 'display': 'inline-block'}), 
    
    html.Div(["Si desea ver un estrato en particular seleccionelo en la casilla: ",
              dcc.Dropdown(
                id='dropdown-6',
                options=[{'label': i, 'value': i} for i in ["No Sabe/Ninguno","Estrato 1","Estrato 2","Estrato 3",
                                                            "Estrato 4","Estrato 5","Estrato 6","Todos"]],value="Todos"),
                html.Br()],
                style={'display': 'inline-block', 'margin-left': '10px','margin-right': '20px','width': '45%', 'float': 'left', 'display': 'inline-block'}), 

    
    
])

tab2=dcc.Tab(label='Resultados',children=[
    html.Div('En esta pestaña se encuentra información relacionada con la información que usted desea conocer'),
    html.Br()
])

pestanas = [tab1, tab2]
tabs = dcc.Tabs(children=pestanas)



app.layout = html.Div([
    html.Div(children=[image]),
    html.Br(),
    html.H6(''' Para hacer uso del sistema de datos es necesario realizar lo siguiente:'''),
    html.Div(" 1. Asegurate de ingresar los datos correctamente en las casillas correspondientes, en caso de que no poseas el dato puedes dejar la casilla en blanco."),
    html.Div(" 2. Cuando ingreses todos los datos, por favor da click en el botón 'Continuar', el cual se encuentra debajo de los datos requeridos. "),
    html.Div(" 3. Finalmente, se mostrará un resumen de los datos, debajo de este, encontrarás gráficas de tu interés y el resultado."),
    
    html.Br(),
    
    html.Div(["Para iniciar, porfavor seleccione que tipo de gráfica prefiere: ",
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
   
    html.Div(["Categoría del Colegio: ",
              dcc.RadioItems(
                id='Radio-3',
                options=[{'label': i, 'value': i} for i in ["Oficial","No Oficial"]],value="Seleccione"),
                html.Br()],
                style={'margin-right': '10px','width': '22%', 'float': 'left'}),
    
    html.Br(),
    
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
    Output('Radio-4', 'value'),
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
    
