from vpython import *
from math import *

# Datos
m1 = 6.0 # masa particula 1
m2 = 6.0 # masa particula 2
R = 10.0 # radio de anillo
d = 100 # densidad
r1 = ((3.0*m1)/(4*pi*d))**(1.0/3) # radio de particula 1
r2 = ((3.0*m2)/(4*pi*d))**(1.0/3) # radio de particula 2
g = 10.0 # fuerza de gravedad
dt = 1.0/60 # intervalos de tiempo
nu = 0.0 # coeficiente de roce cinetico (superficie)

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

theta1 = asin(1.0*P1.pos.z/P1.pos.z) # angulo P1
theta2 = -theta1 # angulo P2
omega1 = 0.1 # vel. angular P1
omega2 = 0.0 # vel. angular P2

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
