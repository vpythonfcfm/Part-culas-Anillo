from vpython import *
from math import *

'''Datos del problema
****** ESCRIBIR DESCRIPCION *******

masa particula 1            : m1
radio planeta (Masa mayor)  : m2
Radio anillo                : R
densidad                    : d
radio particula 1           : r1
radio particula 2           : r2
gravedad                    : g
coeficiente de roce cinetico: nu
tiempo                      : dt
angulo Particula 1          : theta 1
angulo Particula 2          : theta 2
velocidad angular P1        : omega 1
velocidad angular P2        : omega 2

'''

m1 = 6.0 
m2 = 6.0 
R = 10.0  
d = 100 
r1 = ((3.0*m1)/(4*pi*d))**(1.0/3) 
r2 = ((3.0*m2)/(4*pi*d))**(1.0/3) 
g = 10.0 
dt = 1.0/60 
nu = 0.0 
theta1 = asin(1.0*P1.pos.z/P1.pos.z) 
theta2 = -theta1 
omega1 = 0.1 
omega2 = 0.0



# Pelotas
P1 = sphere(pos = vector(0,0,R), radius = r1, color = color.red, make_trail=True, interval = 0.1) # pelota que se encuentra arriba
P2 = sphere(pos = vector(0,0,-R), radius = r2, color = color.blue,  make_trail=False) # pelota que se encuentra abajo

# Ejes
    # Cartesianos
x_i = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_j = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_k = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)
    # Cilindricos
ro_e = arrow(pos = P1.pos, axis=vector(1,0,0), color = color.white, shaftwidth=0.05)
th_e = arrow(pos = P1.pos, axis=vector(0,0,1), color = color.white, shaftwidth=0.05)

def signo(a):
    if a==0:
        return 0
    else:
        return (abs(a)/a)

while True:

    rate(60)

    if (P1.pos-P2.pos).mag-(r1+r2)<=0.08: # realiza la transferencia de momentum
        o1 = omega1
        o2 = omega2
        omega1 =((o1*(m1-m2))+2*o2*m2)/(m1+m2)
        omega2 =((o2*(m2-m1))+2*o1*m1)/(m1+m2)

        
    
    ## datos P1
    a1 = -(g/R)*cos(theta1) - (signo(omega1))*g*abs(sin(theta1))*nu # aceleracion del sistema: gravedad y roce superficial cinético respectivamente
    omega1 = omega1 + a1*dt
    theta1 = theta1 + omega1*dt
    P1.pos.x = R*cos(theta1)
    P1.pos.z = R*sin(theta1)
    ro_e.pos = th_e.pos = P1.pos + r1*ro_e.axis
    ro_e.axis = vector(cos(theta1),0,sin(theta1))
    th_e.axis = omega1*vector(-sin(theta1),0,cos(theta1))

    ## datos P2
    a2=-(g/R)*cos(theta2) - (signo(omega2))*g*abs(sin(theta2))*nu # aceleracion del sistema: gravedad y roce superficial cinético respectivamente
    omega2 = omega2 + a2*dt
    theta2 = theta2 + omega2*dt
    P2.pos.x = R*cos(theta2)
    P2.pos.z = R*sin(theta2)
