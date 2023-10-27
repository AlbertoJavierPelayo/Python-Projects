# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:56:38 2022

@author: beto1
"""

#importacion de librerias

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math



#Parámetros del Motor
Bm = 0.001 #Coeficiente de fricción viscosa del motor
BL =0.001 #Coeficiente de fricción viscosa de la carga
Jm = 0.0078 #Momento de inercia del Motor
Km = 0.83 #Constante del Motor
Kb = 0.83 #Constante de la fem
Ra = 4.5 #Resistencia de Armadura
La = 0.88*(1e-3) #Inductancia de armadura
n1 = 10 #Número de dientes engrane 1
n2 = 50 #Número de dientes engrane 2
JL = 0.1 #Momento de inercia de la carga
######################################################
#Vector de tiempo de Simulación
start = 0
stop = 1
step = 1e-3
t = np.arange(start, stop, step)
######################################################
#Ecuaciones Diferenciales del Sistema Mecatrónico
def f(x, t):
 dx_dt = [0, 0, 0]
 va = 12 #Voltaje de entrada del Motor
 n = (n1/n2)
 Beq = Bm + pow(n, 2) * BL
 Jeq = Jm + pow(n, 2) * JL
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


plt.plot(t, np.sin(t))
plt.grid()
plt.show()



