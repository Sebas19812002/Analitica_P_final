from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination
from pgmpy.estimators import HillClimbSearch
from pgmpy.estimators import K2Score
from pgmpy.readwrite import BIFReader
from pgmpy.estimators import PC
from pgmpy.estimators import BicScore
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
#Tipo es si el modelo es de un .Bif (B) o recien estimado(E), pues el .bif vuelve todo string
def Metricas (test_data, modelo, tipo):
    
    filas=test_data.shape[0]
    nodos=modelo.nodes()
    inferencia = VariableElimination(modelo)    
    tabla = pd.DataFrame(columns=['VP', 'VN', 'FP', 'FN'], index=[0])
    vp=0
    vn=0
    fp=0
    fn=0
    for j in range(0,filas): 
        real=test_data.iloc[j]
        Evidencia={}
        for i in range(0,real.shape[0]-1):
            if  real.index[i] in nodos:
                if tipo=="B" :
                    Evidencia[real.index[i]]=str(real[i])
                elif tipo =="E":
                    Evidencia[real.index[i]]=real[i]
        
        resultado = inferencia.query(['Puntaje_obtenido'], evidence=Evidencia).values
        
        Prediccion="Rechazado"
    
        if resultado[0]>=0.5 :
            Prediccion="Aceptado"
        if Prediccion == real[-1] and Prediccion=="Aceptado"  :
            #Aceptado y  el modelo acerto
            vp+=1
        elif Prediccion == real[-1] and Prediccion=="Rechazado" :
            #No aceptado y el modelo acerto   
            vn+=1
        elif Prediccion != real[-1] and Prediccion=="Rechazado" and real[-1]=="Aceptado" :
            #Aceptado y el modelo no acerto 
            fn+=1
        else:  
            #No aceptado pero el modelo dio positivo
            fp+=1
    tabla.loc[0] = [vp,vn, fp, fn]     
    return(tabla)

df_ent=pd.read_csv("Datos_entrenamiento.csv")
df_prueba= pd.read_csv("Datos_test.csv")   

Aceptados = df_prueba['Puntaje_obtenido'].value_counts()['Aceptado']
Rechazados = df_prueba['Puntaje_obtenido'].value_counts()['Rechazado']

Aceptados = df_ent['Puntaje_obtenido'].value_counts()['Aceptado']
Rechazados = df_ent['Puntaje_obtenido'].value_counts()['Rechazado']



###-------------- Nodos que son importantes y no deben cambiar---------------# 
#-----nodos-------#
edges_fijos=[("estu_genero","Puntaje_obtenido")]
#-------------------------------------------------------------#
#-----------------------Modelo nuestro------------------------#
#-------------------------------------------------------------#

print("#-----------------------Modelo nuestro----------------------------#")
modelo = BIFReader("Modelo.bif").get_model()
modelo.check_model()
print("Nodos y edges\n",modelo.nodes(),"\n",modelo.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo.edges()))
Resultados=Metricas(df_prueba, modelo, "B")
print("Resultados del modelo inicial","\n",Resultados,"\n")

puntajeK2 = K2Score(data=df_ent).score(modelo_estructura)
print("K2 Score","\n",puntajeK2)

puntajeBIC = BicScore(data=df_ent).score(modelo_estructura)
print("BIC Score","\n",puntajeBIC,"\n")





#-------------------------------------------------------------#
#-----------sacar modelo por Hillclimb y score K2 ------------#
#-------------------------------------------------------------#

print("#-----------Modelo por Hillclimb y score K2 ------------#x ")
scoring_method = K2Score(data=df_ent)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df_ent)

modelo_k2 = esth.estimate(fixed_edges=edges_fijos, scoring_method=scoring_method,
                          max_indegree=2) 


modelo_k2 = BayesianNetwork(modelo_k2)
modelo_k2.fit(data=df_ent, estimator = BayesianEstimator)
modelo_k2.check_model()
print("Nodos y edges\n",modelo_k2.nodes(),"\n",modelo_k2.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo_k2.edges()))
Resultados=Metricas(df_prueba, modelo_k2, "E")
print("Resultados del modelo inicial","\n",Resultados,"\n")

puntajeK2 = K2Score(data=df_ent).score(modelo_estructura)
print("K2 Score","\n",puntajeK2)

puntajeBIC = BicScore(data=df_ent).score(modelo_estructura)
print("BIC Score","\n",puntajeBIC,"\n")




#-------------------------------------------------------------#
#----------------Modelo Hillclimb con BIC score---------------#
#-------------------------------------------------------------#

print("#----------------Modelo Hillclimb con BIC score------------------#")
scoring_method = BicScore(data=df_ent)  #Que tanto una variable es influenciada por posibles padres
esth = HillClimbSearch(data=df_ent)
modelo_BIC = esth.estimate(fixed_edges=edges_fijos,
                           scoring_method=scoring_method, max_indegree=2) 
modelo_BIC = BayesianNetwork(modelo_BIC)
modelo_BIC.fit(data=df_ent, estimator = BayesianEstimator)
modelo_BIC.check_model()

print("Nodos y edges\n",modelo_BIC.nodes(),"\n",modelo_BIC.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo_BIC.edges()))
Resultados=Metricas(df_prueba, modelo_BIC, "E")
print("Resultados del modelo inicial","\n",Resultados,"\n")

puntajeK2 = K2Score(data=df_ent).score(modelo_estructura)
print("K2 Score","\n",puntajeK2)

puntajeBIC = BicScore(data=df_ent).score(modelo_estructura)
print("BIC Score","\n",puntajeBIC,"\n")


#-------------------------------------------------------------#
#-----------------------Modelo otro ------------------#
#-------------------------------------------------------------#

print("#-----------------------Modelo otro----------------------------##")
modelo_ = BayesianNetwork([("Educacion_Madre","Personas_hogar"),
                                ("Educacion_Padre","Personas_hogar"),
                                ("Personas_hogar","fami_estratovivienda"),
                                ("fami_estratovivienda","cole_naturaleza"),
                                ("cole_area_ubicacion","cole_naturaleza"),
                                ("cole_naturaleza","Puntaje_obtenido"),
                                ("estu_genero","Puntaje_obtenido"),
                                ("Educacion_Madre","Puntaje_obtenido"),
                                ("Educacion_Padre","Puntaje_obtenido"),
                                ("fami_estratovivienda","Puntaje_obtenido")
                                ])
modelo_.fit(data=df_ent, estimator = BayesianEstimator)

modelo_.check_model()

print("Nodos y edges\n",modelo_.nodes(),"\n",modelo_.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo_.edges()))
Resultados=Metricas(df_prueba, modelo_, "E")
print("Resultados del modelo inicial","\n",Resultados,"\n")

puntajeK2 = K2Score(data=df_ent).score(modelo_estructura)
print("K2 Score","\n",puntajeK2)

puntajeBIC = BicScore(data=df_ent).score(modelo_estructura)
print("BIC Score","\n",puntajeBIC,"\n")


eby = BayesianEstimator(model=modelo_, data=df_ent)

cpd_p1=eby.estimate_cpd(node="Puntaje_obtenido", prior_type="dirichlet", pseudo_counts=[[300]*4032, [150]*4032])
cpd_n=eby.estimate_cpd(node="cole_naturaleza", prior_type="dirichlet", pseudo_counts=[[100000]*14, [1000]*14])
cpd_m=eby.estimate_cpd(node="Educacion_Madre", prior_type="dirichlet", pseudo_counts=[[150000], [7000],
                       [100], [100],[100], [10000],[500], [250],[2000], [1000],
                       [5000], [2500]])
cpd_p=eby.estimate_cpd(node="Educacion_Padre", prior_type="dirichlet", pseudo_counts=[[150000], [7000],
                       [100], [100],[100], [10000],[500], [250],[2000], [1000],
                       [5000], [2500]])

modelo_.add_cpds(cpd_n,cpd_m,cpd_p,cpd_p1)


print(modelo_.get_cpds("Educacion_Madre"))
print(modelo_.get_cpds("Educacion_Padre"))
print(modelo_.get_cpds("cole_naturaleza"))
print(modelo_.get_cpds("Puntaje_obtenido"))

Resultados=Metricas(df_prueba, modelo_, "E")
print("Resultados del modelo inicial","\n",Resultados,"\n")
  

