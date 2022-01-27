# -*- coding: utf-8 -*-
"""
@author: Mayapache
¡PirateⒶ y difunde!
Segunda parte para entender y aplicar la estructura de dancing links

Generación de matriz de celdas para el sudoku (limitantes y elecciones)
     Limitantes: 
         Cada celda con exactamente un número               Cel_Num
         Cada fila con un número 1, un número 2, etc.       Fil_Num
         Cada columna con un número 1, un número 2, etc.    Col_Num
         Cada segmento con un número 1, un número 2, etc.   Seg_Num
     Elecciones posibles:
         9x9x9 (9 filas, 9 columnas, 9 números en cada una)
Toma de elecciones a partir de una matriz de sudoku otorgada
Algoritmo de resolución de sudoku
Traductor sudoku-> matriz-> sudoku

Bibliografía:
    Knuth paper
         https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
    Zendoku (Recomendado)
        https://garethrees.org/2007/06/10/zendoku-generation/#section-4
"""
import numpy as np
import time as tm

class Celda:
    def __init__(self, VinI, VinD, VinAr, VinAb, Sum):
        self.VinI = VinI
        self.VinD = VinD
        self.VinAr = VinAr
        self.VinAb = VinAb
        self.Sum = Sum
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
    if min(vec_Sum)==0:#Revisar si no hay alguna limitante no satisfecha con un 0 (osease, que no hay opcion que la pueda cumplir)
        return False
    
    lim_selec=vec_Lim[vec_Sum.index(min(vec_Sum))]#Seleccionamos una limitante (la de menor valor de Sum)
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
def opcion_elegida(opcion, lim_selec):   #Hubo una selección
    vec_lim_cumplidas=[]  #Vector de limitantes que cumple la opcion seleccionada
    vec_lim_cumplidas=Genera_Vec_Colum(opcion,lim_selec,vec_lim_cumplidas,lim_selec)
    for i in range(len(vec_lim_cumplidas)):
        esconder_lim(vec_lim_cumplidas[i])#Ocultamos los limitantes cumplidos
    for j in range(len(vec_lim_cumplidas)):
        vec_filas_ocul=[]  #Obtenemos filas de cada limitante
        vec_filas_ocul=Genera_Vec_Filas(limitantes[vec_lim_cumplidas[j]].Obten_Ab(),vec_lim_cumplidas[j],vec_filas_ocul)
        for i in range(len(vec_filas_ocul)): #Ocultamos esas filas
            esconder_selec(vec_filas_ocul[i],vec_lim_cumplidas[j],vec_lim_cumplidas[j])

                            #Funciones para Printear y que se vea boneto
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
def printea_sudo(sud):
    print("")
    print("*************************************")
    for i in range(9):
        if i == 3 or i==6:
            print("---------------------------------")
        print(sud[i][0:3],"|",sud[i][3:6],"|",sud[i][6:9])

#  >>>>>>>>>>>>>>>>> CONSTRUIMOS LA MATRIZ PARA LOS SUDOKUS <<<<<<<<<<<<<<<<<
vacio=np.zeros((9,9),dtype=int)
     #Construimos la parte de la matriz que correspnde a que en cada celda haya un número
construc=np.zeros((9,9),dtype=int)
for i in range(9):
    construc[i][0]=1
Cel_Num_Base=construc
for i in range(8):
    construc=np.roll(construc,1,axis=1) #Rolea a la derecha
    Cel_Num_Base=np.concatenate((Cel_Num_Base,construc), 0)  #Uno abajo del otro
Cel_Num_Columna=Cel_Num_Base
for i in range(72):
    Cel_Num_Columna=np.concatenate((Cel_Num_Columna,vacio),0)
Cel_Num=Cel_Num_Columna
for i in range(8):
    Cel_Num_Columna=np.roll(Cel_Num_Columna,81,axis=0) #Rolea pabajo
    Cel_Num=np.concatenate((Cel_Num,Cel_Num_Columna),1) #A la derecha del otro
     #Construimos la parte de la matriz que correspnde a que en cada Fila, haya un 1 y un 2
construc=np.zeros((9,9),dtype=int)
for j in range(9):
    for i in range(9):
        if (i==j):
            construc[i][j]=1
Fil_Num_Base=construc
for i in range(8):
    Fil_Num_Base=np.concatenate((Fil_Num_Base,construc),0) #Abajo del otro
Fil_Num_Columna=Fil_Num_Base
for i in range(72):
    Fil_Num_Columna=np.concatenate((Fil_Num_Columna,vacio),0)
Fil_Num=Fil_Num_Columna
for i in range(8):
    Fil_Num_Columna=np.roll(Fil_Num_Columna,81,axis=0) #Rolea pabajo
    Fil_Num=np.concatenate((Fil_Num,Fil_Num_Columna),1) #A la derecha del otro
    #Construimos la parte de la matriz que correspnde a que en cada Columna, haya un 1 y un 2
construc=np.zeros((9,9),dtype=int)
for j in range(9):
    for i in range(9):
        if (i==j):
            construc[i][j]=1
Col_Num_Base=construc
for i in range(8):
    Col_Num_Base=np.concatenate((Col_Num_Base,vacio),0) #Abajo del otro
Col_Num_Columna=Col_Num_Base
for i in range(8):
    Col_Num_Columna=np.concatenate((Col_Num_Columna,Col_Num_Base),0) #Abajo del otro
Col_Num=Col_Num_Columna
for i in range(8):
    Col_Num_Columna=np.roll(Col_Num_Columna,9,axis=0) #Rolea pabajo
    Col_Num=np.concatenate((Col_Num,Col_Num_Columna),1) #A la derecha del otro
    #Construimos la parte de la matriz que correspnde a que en cada Segmento, haya un 1 y un 2
construc=np.zeros((9,9),dtype=int)
for j in range(9):
    for i in range(9):
        if (i==j):
            construc[i][j]=1
Seg_Num_Base=construc
for i in range(2):
    Seg_Num_Base=np.concatenate((Seg_Num_Base,construc),0) #Abajo del otro
for i in range(6):
    Seg_Num_Base=np.concatenate((Seg_Num_Base,vacio),0) #Abajo del otro
Seg_Num_Columna=Seg_Num_Base
for i in range(2):
    Seg_Num_Columna=np.concatenate((Seg_Num_Columna,Seg_Num_Base),0) #Abajo del otro
for i in range(54):
    Seg_Num_Columna=np.concatenate((Seg_Num_Columna,vacio),0) #Abajo del otro
Seg_Num_aux=Seg_Num_Columna
for i in range(2):
    Seg_Num_Columna=np.roll(Seg_Num_Columna,27,axis=0) #Rolea pabajo
    Seg_Num_aux=np.concatenate((Seg_Num_aux,Seg_Num_Columna),1) #A la derecha del otro
Seg_Num=Seg_Num_aux
for i in range(2):
    Seg_Num_aux=np.roll(Seg_Num_aux,243,axis=0) #Rolea pabajo
    Seg_Num=np.concatenate((Seg_Num,Seg_Num_aux),1) #A la derecha del otro
    #Construimos la matriz completa
Matriz_Sudoku=np.concatenate((Cel_Num,Fil_Num,Col_Num,Seg_Num),1)

mat=Matriz_Sudoku

limitantes=[]
num_lim=len(mat[0])+1
for i in range(num_lim):
    limitantes.append(Celda(None,None,None,None,None))
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
        filita.append(Celda(None,None,None,None,None))
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

sudoku=[                        #_contra
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,3,0,8,5],
        [0,0,1,0,2,0,0,0,0],
        
        [0,0,0,5,0,7,0,0,0],
        [0,0,4,0,0,0,1,0,0],
        [0,9,0,0,0,0,0,0,0],
        
        [5,0,0,0,0,0,0,7,3],
        [0,0,2,0,1,0,0,0,0],
        [0,0,0,0,4,0,0,0,9]
]

#Extraer las hileras del sudoku a las selecciones en la matriz
#Colocar esas selecciones en la matriz, modificandola
print("sudoku a resolver:")
printea_sudo(sudoku)

#****************Llenamos los valores de Sum en las limitantes, la 1ra vez :D
for i in range (len(limitantes)-1):
    vinculo=limitantes[i].Obten_Ab()
    limitantes[i].Cambia_Sum(Genera_Sum(vinculo,i))
#printea_matriz()
#printea_limitantes()
vec_Sol=[] #vector de solucion
#Todo listo pa la funcion

conta=-1
for i in range(9):
    for j in range(9):
        conta=conta+1
        if sudoku[i][j]!=0:
            opcion_elegida(conta*9+sudoku[i][j]-1,conta)

inicio=tm.time()
funcion_magica()
final=tm.time()

print("Tiempo de ejecución: ",final-inicio)
#Pasar del vector del soluciones a sudoku

vec_sudokito_val=[]
for i in range(len(vec_Sol)):
    vec_sudokito_val.append(vec_Sol[i]%9+1)

vec_sudokito_celda=[]
for i in range(len(vec_Sol)):
    vec_sudokito_celda.append(vec_Sol[i]//9)

vec_sudokito_fila=[]
for i in range(len(vec_Sol)):
    vec_sudokito_fila.append(vec_sudokito_celda[i]//9)

vec_sudokito_col=[]
for i in range(len(vec_Sol)):
    vec_sudokito_col.append(vec_sudokito_celda[i]%9)

for i in range(len(vec_Sol)):
    sudoku[vec_sudokito_fila[i]][vec_sudokito_col[i]]=vec_sudokito_val[i]
printea_sudo(sudoku)
