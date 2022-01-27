# -*- coding: utf-8 -*-
"""
@author: Mayapache
¡PirateⒶ y difunde!
Segunda parte para entender y aplicar la estructura de dancing links

Vector de limitantes    :D listo
Matriz                  :D listo
Conexiones generadas a partir de la matriz de 0's y 1's otorgada    :D listo

Seleccionar columna     x-x
Seleccionar fila        x-x
Algoritmo de resolución     x-x

"""

import numpy as np

class Celda:
    def __init__(self, VinI, VinD, VinAr, VinAb, Fil, Col, Sum):
        self.VinI = VinI
        self.VinD = VinD
        self.VinAr = VinAr
        self.VinAb = VinAb
        self.Sum = Sum
        self.Fil = Fil
        self.Col = Col
    def Cambia_I(self,nuevo_I):
        self.VinI=nuevo_I
    def Cambia_D(self,nuevo_D):
        self.VinD = nuevo_D
    def Cambia_Ar(self,nuevo_Ar):
        self.VinAr=nuevo_Ar
    def Cambia_Ab(self,nuevo_Ab):
        self.VinAb=nuevo_Ab
    def Obten_I(self):
        return self.VinI
    def Obten_D(self):
        return self.VinD
    def Obten_Ar(self):
        return self.VinAr
    def Obten_Ab(self):
        return self.VinAb
    
    def Cambia_Sum(self,nueva_Sum):
        self.Sum=nueva_Sum
    def Mas1_Sum(self):
        self.Sum=self.Sum+1
    def Men1_Sum(self):
        self.Sum=self.Sum-1
    def Obten_Sum(self):
        return self.Sum
    def Obten_Fil(self):
        return self.Fil
    def Obten_Col(self):
        return self.Col


 #Obtenemos la cantidad de filas que podrian llenar la limitante :D
def Genera_Sum(fil,col):
    vinculo=matriz[fil][col].Obten_Ab()
    if vinculo==len(mat):
        return 1
    else:
        return Genera_Sum(vinculo,col)+1

def Genera_Vec_Sum(col,vec_Sum,vec_Lim):
    if col==len(mat[0]):
        return [],[]
    vec_Sum.append(limitantes[col].Obten_Sum())
    vec_Lim.append(col)
    vinculo=limitantes[col].Obten_D()
    if vinculo==len(mat[0]):
        return vec_Sum, vec_Lim
    else:
        return Genera_Vec_Sum(vinculo, vec_Sum, vec_Lim)




def Genera_Vec_Filas(fil,col,vector):   
    if fil==len(mat):
        return vector
    vector.extend([fil])
    vinculo=matriz[fil][col].Obten_Ab()
    if vinculo==len(mat):
        return vector
    else:
        return Genera_Vec_Filas(vinculo,col,vector)


def Genera_Vec_Colum(fil,col,vector,col_in):
    vector.extend([col])
    vinculo=matriz[fil][col].Obten_D()
    if vinculo==col_in:
        return vector
    else:
        return Genera_Vec_Colum(fil,vinculo,vector,col_in)




def esconder_lim(esconde):
    #Logica:
    #a mi izquierda, en su VinD, pongo mi VinD
    #a mi derecha, en su VinI, pongo mi VinI
    mi_i=limitantes[esconde].Obten_I()
    mi_d=limitantes[esconde].Obten_D()
    limitantes[mi_i].Cambia_D(mi_d)
    limitantes[mi_d].Cambia_I(mi_i)

def mostrar_lim(muestra):
    #Logica:
    #A mi izquierda, en su VinD, me pongo a mi
    #A mi derecha, en su VinI, me pongo a mi
    mi_i=limitantes[muestra].Obten_I()
    mi_d=limitantes[muestra].Obten_D()
    limitantes[mi_i].Cambia_D(muestra)
    limitantes[mi_d].Cambia_I(muestra)

def printea_limitantes():
    print("#\tVinI\tVinD\tVinAr\tVinAb\tSum")
    for i in range (num_lim):
        print(i,"\t",limitantes[i].Obten_I(),"\t",limitantes[i].Obten_D(), "\t",limitantes[i].Obten_Ar() , "\t",limitantes[i].Obten_Ab(), "\t",limitantes[i].Obten_Sum())


def printea_matriz():
    print("#\tVinI\tVinD\tVinAr\tVinAb")
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            print(i,",",j,"\t",matriz[i][j].Obten_I(), "\t",matriz[i][j].Obten_D(), "\t",matriz[i][j].Obten_Ar() , "\t",matriz[i][j].Obten_Ab())


def printea_matriz_pro():
    print("#\tVinI\tVinD\tVinAr\tVinAb")
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j].Obten_I()!=None:
                print(i,",",j,"\t", matriz[i][j].Obten_I(), "\t",matriz[i][j].Obten_D(), "\t",matriz[i][j].Obten_Ar() , "\t",matriz[i][j].Obten_Ab())

def esconder_selec(esconde,col,col_in): # se esconde de forma vertical :D
    #Logica:
    #Arriba de mi, en su VinAb, pongo mi VinAb
    #Abajo de mi, en su VinAr, pongo mi VinAr
    #Resto1 a la limitante
    mi_ab=matriz[esconde][col].Obten_Ab()
    mi_ar=matriz[esconde][col].Obten_Ar()
    # Limitantes conectadas pero no en matriz >:00 D:

    if mi_ab !=len(mat):
        matriz[mi_ab][col].Cambia_Ar(mi_ar)
    else:
        limitantes[col].Cambia_Ar(mi_ar)
    if mi_ar !=len(mat):    
        matriz[mi_ar][col].Cambia_Ab(mi_ab)
    else:
        limitantes[col].Cambia_Ab(mi_ab)
    
    limitantes[col].Men1_Sum() #Le restamos un uno a la Sum
    
    vinculo=matriz[esconde][col].Obten_D()
    if vinculo==col_in:
        return
    else:
        esconder_selec(esconde,vinculo,col_in)


# *******************************
        #*************************
        #Cambiando para mostrar la linea/seleccion indicada :D
        
        
def mostrar_selec(muestra,col,col_in): # se muestra de forma vertical :D
    #Logica:
    #Arriba de mi, en su VinAb, me pongo a m
    #Abajo de mi, en su VinAr, me pongo a mi
    #Sumo 1 a la limitante
    mi_ab=matriz[muestra][col].Obten_Ab()
    mi_ar=matriz[muestra][col].Obten_Ar()
    # Limitantes conectadas pero no en matriz >:00 D:

    if mi_ab !=len(mat):
        matriz[mi_ab][col].Cambia_Ar(muestra)
    else:
        limitantes[col].Cambia_Ar(muestra)
    if mi_ar !=len(mat):    
        matriz[mi_ar][col].Cambia_Ab(muestra)
    else:
        limitantes[col].Cambia_Ab(muestra)
    
    limitantes[col].Mas1_Sum() #Le sumamos un uno a la Sum
    
    vinculo=matriz[muestra][col].Obten_D()
    if vinculo==col_in:
        return
    else:
        mostrar_selec(muestra,vinculo,col_in)





def funcion_magica():
    # ___xxx***######################## Empieza la resolución del problema ###########################***xxx___
# *********************** Seleccionamos limitante
#Revisar si no hay alguna limitante no satisfecha con un 0 (osease, que no hay opcion que la peuda cumplir)
    #En caso de que sí, se cancela y se regresa
    #en caso de que no, seguimos
#Elegimos la limitante con el menor numero de opciones/filas disponibles
#Ocultamos la limitane

#Aquí empieza la funcioooon <3
    #Generar vector de los valores de Sum de las limitantes disponibles :D
    vec_Sum=[]
    vec_Lim=[]
    vec_Sum, vec_Lim = Genera_Vec_Sum(limitantes[-1].Obten_D(),vec_Sum, vec_Lim) #Limitante de hasta la derecha, la que lo controla todo, nos vamos a la derecha con el primer vinculo que vea

    if not vec_Sum:
        return True
    if min(vec_Sum)==0:#Revisar si no hay alguna limitante no satisfecha con un 0 (osease, que no hay opcion que la peuda cumplir)
        return False
    
    lim_selec=vec_Lim[vec_Sum.index(min(vec_Sum))]#Seleccionamos una limitante (la de menor velor de Sum)  
    #::::::      Seleccionamos fila, Dentro de la limitación seleccionada
    vec_Opc=[] #Generar vector de filas/opciones disponibles acorde a la limitación seleccionada
    vec_Opc=Genera_Vec_Filas(limitantes[lim_selec].Obten_Ab(),lim_selec,vec_Opc)
    
    for k in range(len(vec_Opc)):
        vec_Sol.append(vec_Opc[k]) #Seleccionamos una opción/Fila :D y la agregamos al set de soluciones
        #::::::     Vector de filas que coinciden en uno o más restricciones con el seleccionado
        vec_lim_cumplidas=[]  #Vector de limitantes que cumple la opcion seleccionada
        vec_lim_cumplidas=Genera_Vec_Colum(vec_Sol[-1],lim_selec,vec_lim_cumplidas,lim_selec)
        vec_filas_ocultadas=[]
        vec_lim_usada_ocultadas=[]
        for i in range(len(vec_lim_cumplidas)):
            esconder_lim(vec_lim_cumplidas[i])#Ocultamos los limitantes cumplidos
        
        for j in range(len(vec_lim_cumplidas)):
            vec_filas_ocul=[]  #Obtenemos filas de cada limitante
            vec_filas_ocul=Genera_Vec_Filas(limitantes[vec_lim_cumplidas[j]].Obten_Ab(),vec_lim_cumplidas[j],vec_filas_ocul)
            for i in range(len(vec_filas_ocul)): #Ocultamos esas filas
                esconder_selec(vec_filas_ocul[i],vec_lim_cumplidas[j],vec_lim_cumplidas[j])
                vec_filas_ocultadas.append(vec_filas_ocul[i])
                vec_lim_usada_ocultadas.append(vec_lim_cumplidas[j])
        if funcion_magica():
            return True
        else: #volvemos a mostrar, porque #RamaMuerta, D: recuerda debe ser alreves (falta*****)
            for i in range(len(vec_lim_cumplidas)):
                mostrar_lim(vec_lim_cumplidas[len(vec_lim_cumplidas)-1-i])#Ocultamos los limitantes cumplidos
            vec_filas_ocultadas.reverse()
            vec_lim_usada_ocultadas.reverse()
            for i in range(len(vec_filas_ocultadas)):
                mostrar_selec(vec_filas_ocultadas[i],vec_lim_usada_ocultadas[i],vec_lim_usada_ocultadas[i])
            vec_Sol.pop(-1)

'''
Algoritmo= 
1.-     Seleccionamos una limitante no satisfecha - alguna columna -> la de menor valor de S
2.-     Seleccionamos una fila dentro de esa columna que satisfaga la limitante
         En caso de no haber, es una rama muerta y regresamoooos
3.-     Aladimos la fila al set de soluciones
4.-     Borramos las columnas ya satisfechas
5.-     Borramos las filas que cumplen con la misma limitante
6.-     Regreso al 1
'''



#Generamos la matriz a partir de 1's
#Esta es una matriz de prueba
#Respuestas=  3,0,4
#              A B C D E F G
mat=np.array([[0,0,1,0,1,1,0],  #0   
              [1,0,0,1,0,0,1],  #1
              [0,1,1,0,0,1,0],  #2
              [1,0,0,1,0,0,0],  #3
              [0,1,0,0,0,0,1],  #4
              [0,0,0,1,1,0,1]]) #5
    #Generamos celdas de arriba (las limitantes)


'''
mat=np.array([[0,1,1,0],  #0   
              [1,0,1,0],  #1
              [1,0,0,0],  #2
              [0,1,0,1],  #3
              [0,0,1,1]]) #5
'''


limitantes=[]
num_lim=len(mat[0])+1
for i in range(num_lim):
    limitantes.append(Celda(None,None,None,None,None,None,None))

#Conectamos limitantes
for i in range(num_lim-1):
    limitantes[i].Cambia_D(i+1)
    
for i in range(1,num_lim):
    limitantes[i].Cambia_I(i-1)
limitantes[0].Cambia_I(num_lim-1)
limitantes[num_lim-1].Cambia_D(0)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXX Generamos matriz XXXXXXXXXXXXXXXXXXXXXXXXXXX
matriz=[]
for fil in range(len(mat)):
    filita=[]
    for col in range(len(mat[0])):
        filita.append(Celda(None,None,None,None,fil,col,None))
    matriz.append(filita)

#Conectamos matriz de objetos a partir de los 1's de la matriz inicial

unos_pos=np.argwhere(mat==1)
#***************************** Conectamos horizontal ***********************

#Generamos matriz de horizontales
horiz_mat=[]
horiz=[]
renglon=0
for i in range(len(unos_pos)):
    if unos_pos[i][0] !=renglon:
        horiz_mat.append(horiz)
        horiz=[]
        renglon+=1
    horiz.append(unos_pos[i][1])
horiz_mat.append(horiz)
#Generamos los vinculos
for j in range(len(horiz_mat)):
    horiz=horiz_mat[j]
    #A la derecha
    for i in range(len(horiz)-1):
        matriz[j][horiz[i]].Cambia_D(horiz[i+1])
    #Extremo derecha
    matriz[j][horiz[-1]].Cambia_D(horiz[0])
    #A la izquierda
    for i in range(1,len(horiz)):
        matriz[j][horiz[i]].Cambia_I(horiz[i-1])
    #Extremo Izquierda
    matriz[j][horiz[0]].Cambia_I(horiz[-1])
    
#***************************** Conectamos vertical ************************
#Generamos matriz de verticales
unos_pos=np.argwhere(mat==1)
unos_pos=unos_pos[np.argsort(unos_pos[:,1])]
verti_mat=[]
verti=[]
columna=0
for i in range(len(unos_pos)):
    if unos_pos[i][1] !=columna:
        verti_mat.append(verti)
        verti=[]
        columna+=1
    verti.append(unos_pos[i][0])
verti_mat.append(verti)
#Generamos los vinculos
for j in range(len(verti_mat)): #recorremos columnas
    verti=verti_mat[j]  #seleccionamos los 1's que hay de tal columna 
    #Abajo    
    for i in range(len(verti)-1):
        matriz[verti[i]][j].Cambia_Ab(verti[i+1])    
    #Hasta abajo va con limitantes
    matriz[verti[-1]][j].Cambia_Ab(len(mat))    
    #Arriba
    for i in range(1,len(verti)):
        matriz[verti[i]][j].Cambia_Ar(verti[i-1])
    #Hasta arriba va con limitantes
    matriz[verti[0]][j].Cambia_Ar(len(mat))
    limitantes[j].Cambia_Ab(verti[0])
    limitantes[j].Cambia_Ar(verti[-1])
#Vínculos formaaaaadoooos en la matriz :DDDDDDDDDDDDDD
    
#****************Llenamos los valores de Sum en las limitantes, la 1ra vez :D
for i in range (len(limitantes)-1):
    vinculo=limitantes[i].Obten_Ab()
    limitantes[i].Cambia_Sum(Genera_Sum(vinculo,i))
#printea_matriz()
#printea_limitantes()

vec_Sol=[] #vector de solucion



#Todo listo pa la funcion

funcion_magica()
print("La solución de la matriz: ")
print(mat)
print("Son los renglones")
print(vec_Sol)
print("Que seleccionados se ven así")
print(mat[vec_Sol])
