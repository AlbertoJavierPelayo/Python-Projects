# -*- coding: utf-8 -*-
#Karla Denise Ortiz Marroquín        -    A01177158
#Luis Gustavo Soto Acuña            -    A00226876
#Miguel Angel Briseño Flores        -    A01630813
#Omar Francisco Morales Becerril    -    A01634007
#Alberto Javier Pelayo Brambila    -    A01636406

#importacion de librerias

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math



#Parámetros del Motor
Ra = 4.5 #Resistencia de Armadura
La = 0.88*(1e-3) #Inductancia de armadura
Kb = 0.83 #Constante de la fem
Km = 0.83 #Constante del Motor
Jm = 0.0078 #Momento de inercia del Motor
JL1 = 0.009 #Momento de inercia de la carga 1
JL2 = 0.020 #Momento de inercia de la carga 2
Bm = 0.001 #Coeficiente de fricción viscosa del motor
BL1 =0.001 #Coeficiente de fricción viscosa de la carga 1
BL2 =0.001 #Coeficiente de fricción viscosa de la carga 1
n1 = 10 #Número de dientes engrane 1
n2 = 50 #Número de dientes engrane 2
n3 = 20 #Número de dientes engrane 1
n4 = 40 #Número de dientes engrane 2

######################################################
#Vector de tiempo de Simulación
start = 0
stop = 4*math.pi 
step = 1e-3
t = np.arange(start, stop, step)
######################################################
#Ecuaciones Diferenciales del Sistema Mecatrónico
def f(x, t):
 dx_dt = [0, 0, 0]
 va = 12*np.sin(t) #Voltaje de entrada del Motor
 n12 = (n1/n2)
 n34 = (n3/n4)
 Jeq = Jm + (pow(n12, 2) * JL1) + (pow(n12, 2) * pow(n34, 2) * JL2)
 Beq = Bm + (pow(n12, 2) * BL1) + (pow(n12, 2) * pow(n34, 2) * BL2)
 dx_dt[0] = x[1]
 dx_dt[1] = -(Beq/Jeq) * x[1] + (Km/Jeq) * x[2]
 dx_dt[2] = -(Kb/La) * x[1] - (Ra/La) * x[2] + (1/La) * va
 return dx_dt
####################################################################
#Solución de las Ecuaciones Diferenciales del Sistema Mecatronico
Sol = odeint(f, y0 = [0, 0, 0], t=t)
print(Sol)
####################################################################
#Graficas
#Posición Angular del Motor
plt.plot(t, Sol[:, 0], 'b', label='x1(t)')
plt.xlabel('t (segundos)')
plt.ylabel('x1')
plt.title('Posición Angular (Rad)')
plt.grid()
plt.show()
#Velocidad Angular del Motor
plt.plot(t, Sol[:, 1], 'b', label='x2(t)')
plt.xlabel('t (segundos)')
plt.ylabel('x2')
plt.title('Velocidad Angular (Rad/s)')
plt.grid()
plt.show()
#Corriente de Armadura del Motor
plt.plot(t, Sol[:, 2], 'r', label='x3(t)')
plt.xlabel('t (segundos)')
plt.ylabel('x3')
plt.title('Corriente de Armadura (Amp)')
plt.grid()
plt.show()

#Voltaje de entrada del Motor
va = 12*np.sin(t)
plt.plot(t, va, 'g', label='Va(t)')
plt.xlabel('t (segundos)')
plt.ylabel('Va')
plt.title('Voltaje de entrada del motor (V)')
plt.grid()
plt.show()


