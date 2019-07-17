# movimiento aleatório en 3 dimensiones, pasos normalizados
from vpython import *
import numpy as np
import random as rd
scene.range = 100 # se define la dimensión de la escena 
#flecha para los vectores que definen el sistema coordenado
X = arrow(pos=vec(-5,0,0), axis=vec(20,0,0), color=color.red) # Eje x
label(pos=vec(0,0,0), text='X')
Y = arrow(pos=vec(-5,0,0), axis=vec(0,20,0), color=color.green) # Eje y
label(pos=vec(-5,5,0), text='Y')
Z = arrow(pos=vec(-5,0,0), axis=vec(0,0,20)) # Eje z
label(pos=vec(-5,0,5), text='Z')
#Creación de objetos (a.k.a partículas): se define su posición inicial, dimensiones, color y que se mantenga visible su trayectoria
particula1 = sphere(pos = vec(-5,0,0),radius = 0.5, color = color.red, make_trail = True)
particula2 = sphere(pos = vec(-5,0,0),radius = 0.5, color = color.blue, make_trail = True)
particula3 = sphere(pos = vec(-5,0,0),radius = 0.5, color = color.white, make_trail = True)

# parámetros
N = 1000 # número de pasos a realizar
semilla = 3 # semilla para reproducibilidad
cont = 0 # variable de conteo de pasos
while(cont < N):
    rate(20) # fotogramas por segundo
    # actualización de posiciones con un paso aleatório
    particula1.pos  = particula1.pos + vec((rd.random()-0.5)*2,(rd.random()-0.5)*2,(rd.random()-0.5)*2) 
    particula2.pos  = particula2.pos + vec((rd.random()-0.5)*2,(rd.random()-0.5)*2,(rd.random()-0.5)*2)
    particula3.pos  = particula3.pos + vec((rd.random()-0.5)*2,(rd.random()-0.5)*2,(rd.random()-0.5)*2)
