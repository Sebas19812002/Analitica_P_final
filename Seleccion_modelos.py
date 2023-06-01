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
        
        resultado = inferencia.query(['diagnosis'], evidence=Evidencia).values
        
        Prediccion=1
        #Prob de no tener = 0
        if resultado[0]>=0.5 :
            Prediccion=0
        if Prediccion == real[-1] and Prediccion==1  :
            #Tiene la enfermedad el modelo acerto
            vp+=1
        elif Prediccion == real[-1] and Prediccion==0 :
            #No tiene la enfermedad y el modelo acerto   
            vn+=1
        elif Prediccion != real[-1] and Prediccion==0 and real[-1]==1 :
            #Tiene la enfermedad y el modelo no acerto 
            fn+=1
        else:  
            #No tiene la enfermedad pero el modelo dio positivo
            fp+=1
    tabla.loc[0] = [vp,vn, fp, fn]     
    return(tabla)

df_ent=pd.read_csv("Datos_entrenamiento.csv")
df_prueba= pd.read_csv("Datos_test.csv")

###-------------- Nodos que son importantes y no deben cambiar---------------# 
#-----Padres---------#
padres={"sex":0, "age":0}
#-----nodos-------#
edges_fijos=[("diagnosis","ecg"),("age","pressure"),("sex","pressure"),("sugar","chol")]
black_list =[("chol","sex"),("maxbpm","age"),("diagnosis","sex"),("diagnosis","age"), ('thal', 'sex')]

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
#--------------Modelo estimado por PC sin nada nuevo----------#
#-------------------------------------------------------------#

print("#--------------Modelo estimado por PC sin nada nuevo--------------##")
est = PC(data=df_ent)
modelo_PC = est.estimate(variant="stable", max_cond_vars=5)
modelo_PC = BayesianNetwork(modelo_PC)
modelo_PC.fit(data=df_ent, estimator = BayesianEstimator)
modelo_PC.check_model() 
print("Nodos y edges\n",modelo_PC.nodes(),"\n",modelo_PC.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo_PC.edges()))
Resultados=Metricas(df_prueba, modelo_PC, "E")
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
                          max_indegree=5, black_list=black_list) 
modelo_k2=esth.estimate()
#max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
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
                           scoring_method=scoring_method, max_indegree=5,black_list=black_list) #max indegree es el numero de padres maximosn max_inter es el numero de pasos a iterar el Hillclimb
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
#-----------------------Modelo de otro grupo------------------#
#-------------------------------------------------------------#

print("#-----------------------Modelo de otro grupo----------------------------##")
modelo_ = BayesianNetwork([("sex", "chol"),
                           ("age", "chol"),
                           ("age", "sugar"),
                           ("thal", "pressure"),
                           ("chol", "diagnosis"),
                           ("sugar", "pressure"),
                           ("pressure", "diagnosis"),
                           ("diagnosis", "flourosopy"),
                           ("diagnosis", "maxbpm"),
                           ("diagnosis", "angina"),
                           ("diagnosis", "ecg"),
                           ("angina", "cpt"),
                           ("cpt", "oldpeak"),
                           ( "ecg","oldpeak"),
                           ("ecg","slope")])
modelo_.fit(data=df_ent, estimator = BayesianEstimator)
modelo_.check_model()
print("Nodos y edges\n",modelo_.nodes(),"\n",modelo_.edges(),"\n")

modelo_estructura=BayesianNetwork(list(modelo.edges()))
Resultados=Metricas(df_prueba, modelo_, "E")
print("Resultados del modelo inicial","\n",Resultados,"\n")

puntajeK2 = K2Score(data=df_ent).score(modelo_estructura)
print("K2 Score","\n",puntajeK2)

puntajeBIC = BicScore(data=df_ent).score(modelo_estructura)
print("BIC Score","\n",puntajeBIC,"\n")

