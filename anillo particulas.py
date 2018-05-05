from vpython import *
from math import *

# Datos
R = 10.0 # radio de anillo
r = 0.2 # radio de particulas
m1 = 6.0
m2 = 6.0
g = 10.0
dt = 1.0/60

# Pelotas
P1 = sphere(pos = vector(0,0,R), radius = 1*r, color = color.red, make_trail=True, interval = 1) # esfera que se encuentra arriba
P2 = sphere(pos = vector(0,0,-R), radius = r, color = color.blue)

# Ejes
    # Cartesianos
x_i = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_j = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_k = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)
    # Cilindricos
ro_e = arrow(pos = P1.pos, axis=vector(1,0,0), color = color.red, shaftwidth=0.05)
th_e = arrow(pos = P1.pos, axis=vector(0,0,1), color = color.red, shaftwidth=0.05)

theta1 = asin(1.0*P1.pos.z/P1.pos.z)
theta2 = -theta1
omega1 = 0.1
omega2 = 0



while True:

    rate(60)

    if (P1.pos-P2.pos).mag-2*r<=0.08: # realiza la transferencia de momentum
        o1 = omega1
        o2 = omega2
        omega1 =((o1*(m1-m2))+2*o2*m2)/(m1+m2)
        omega2 =((o2*(m2-m1))+2*o1*m1)/(m1+m2)
            
        
    
    ## datos P1
    a1=-(g/R)*cos(theta1)
    omega1 = omega1 + a1*dt
    theta1 = theta1 + omega1*dt
    P1.pos.x = R*cos(theta1)
    P1.pos.z = R*sin(theta1)
    ro_e.pos = th_e.pos = P1.pos
    ro_e.axis = vector(cos(theta1),0,sin(theta1))
    th_e.axis = vector(-sin(theta1),0,cos(theta1))

    ## datos P2
    a2=-(g/R)*cos(theta2)
    omega2 = omega2 + a2*dt
    theta2 = theta2 + omega2*dt
    P2.pos.x = R*cos(theta2)
    P2.pos.z = R*sin(theta2)
